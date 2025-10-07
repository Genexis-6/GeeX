from fastapi import APIRouter, Depends, BackgroundTasks, Request, Response, status
from app.repo import db_injection
from app.repo.schemas.request_schemas.users.users_auth.create_user_acc import CreateUserAccountSchemas
from app.repo.schemas.response_schemas.users.user_auths.registration_response import RegistrationRes
from app.repo.schemas.response_schemas import DefaultApiResponse
from app.utils.enums.auth_enums import AuthEnums
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.security.jwt_tokens.token_generators import generate_access_token, generate_refresh_token, verify_token
from app.utils.enums.jwt_roles import JWTroles
from datetime import timedelta
from app.repo.queries.auth_queries.user_auth_queries import UsersAuthQueries
from app.utils.helpers.cache_refresh_token_id import cache_session_token_id, get_cache_refresh_token
import uuid
from typing_extensions import Annotated



auth = APIRouter(
    prefix="/auth",
    responses={
        404:{
            "message": "not found"
        }
    },
    tags=["auth"],
)



@auth.post("/register", response_model=DefaultApiResponse[RegistrationRes])
async def register(db: db_injection, user: CreateUserAccountSchemas):
    user_query = UsersAuthQueries(db)
    res = await user_query.create_user_account(user)
    if res == AuthEnums.EXIST:
        return JSONResponse(
            content={
                "message": "seller with this email exist",
                }, 
            status_code= status.HTTP_403_FORBIDDEN
            )
    
    if res == AuthEnums.INVALID_PHONE_NUMBER:
        return JSONResponse(
            content={
                "message": "phone number fommart not allowed",
                },
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT
        )
    return DefaultApiResponse(
        message="account created",
        status_code=201,
        data={
            "name":user.name
        }
    )
    
    

@auth.post("/login")
async def login(db: db_injection, response: Response,background_task: BackgroundTasks, form_data: OAuth2PasswordRequestForm = Depends()):
    sellers_query = UsersAuthQueries(db)
    res = await sellers_query.login_user(form_data)
    if res == AuthEnums.ERROR:
        raise HTTPException(
            detail="error login in",
            status_code=500,
        )
    if res == AuthEnums.NONE_FOUND:
        raise HTTPException(
            detail="no user with this email found",
            status_code=404
        )
    if res == AuthEnums.ACCECC_NOT_GRANTED:
        raise HTTPException(
            detail="incorrect password",
            status_code=403
        )
    access_token = generate_access_token(
            id=str(res.id),
            username=res.name,
            email=res.email,
            exp_time= timedelta(minutes=10),
            role=str(JWTroles.SELLER)
        )
    refresh_token= generate_refresh_token(
            id=str(res.id),
            username=res.name,
            email=res.email,
            role=str(JWTroles.SELLER.value)
        )
    background_task.add_task(cache_session_token_id, token=refresh_token, id=str(res.id))

    response.set_cookie(
        key="token_id",
        value=str(res.id),
        expires=604800,
        httponly=True,
        path="",
        secure=True,
        samesite="lax"
    )
     
    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
        
@auth.get("/get_current_user", response_model= DefaultApiResponse)
async def get_current_user(current_user:Annotated[dict, Depends(verify_token)]):
    return DefaultApiResponse(
        status_code=200,
        message="user info",
        data=current_user
    )



@auth.get("/refresh_token")
async def refresh_token(request:Request):
    try:
        get_token_id = request.cookies.get("token_id")
        refresh_token = await get_cache_refresh_token(get_token_id)
        if refresh_token == AuthEnums.FAILED:
            raise HTTPException(
                detail="error getting refresh token",
                status_code= 401
            )
        
        if refresh_token is None:
            raise HTTPException(
                detail="No refresh token found",
                status_code=401
            )
        if refresh_token == AuthEnums.ERROR:
            raise HTTPException(
                detail="Network error: service not avaliable",
                status_code=503
            )
        data:dict = await verify_token(refresh_token)


        access_token  = generate_access_token(
            id=data.get("id"),
            username=data.get("username"),
            email=data.get("email"),
            exp_time= timedelta(minutes=10),
            role=data.get("role")
        )
        return {
            "access_token": access_token,
            "new_token": "Bearer"
        }
    except Exception as e:
        raise HTTPException(
            detail=f"error getting new token due to: {e}",
            status_code=500
        )