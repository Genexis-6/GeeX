from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Optional
from datetime import timedelta, datetime
from app.utils.enums.jwt_roles import JWTroles
from app.config.env_config.dev_config import dev_config
import jwt
from jwt.exceptions import DecodeError, ExpiredSignatureError, InvalidSignatureError
from fastapi.exceptions import HTTPException
from fastapi import Depends
from typing_extensions import Annotated




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")
SK = dev_config.SK
ALGO = dev_config.ALGO

def generate_access_token(id: str,email: str, username: str, role: JWTroles , exp_time:Optional[timedelta] = None):
    to_ecode = {
        "id":id,
        "sub":id,
        "email": email,
        "username": username,
        "role": role,
    }
    
    if exp_time:
        exp = datetime.utcnow() + exp_time
    else:
        exp = datetime.utcnow() + timedelta(minutes=10)
    to_ecode.update({"exp": exp})
    return jwt.encode(to_ecode, SK, algorithm=ALGO)



def generate_refresh_token(id: str,email: str, username: str, role: JWTroles):
    to_ecode = {
        "id":id,
        "sub":id,
        "email": email,
        "username": username,
        "role": role,
        "exp": datetime.utcnow() + timedelta(minutes=7)
    }
    return jwt.encode(to_ecode, SK, algorithm=ALGO)





async def verify_token(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload: dict = jwt.decode(token, SK, algorithms=[ALGO])
        user_id:str = payload.get("id")
        user_email: str = payload.get("email")
        user_name: str = payload.get("username")
        role = payload.get("role")
        exp = payload.get("exp")
        
        return {
            "user_id": user_id,
            "user_email": user_email,
            "user_name": user_name,
            "role": role,
            "exp": exp
        }
    except ExpiredSignatureError as e:
        print(f"error due to: {e}")
        raise HTTPException(detail="token has expired", status_code= 401)
    except DecodeError as e:
        print(f"error due to: {e}")
        raise HTTPException(detail="error decoding token", status_code= 401)  
    except InvalidSignatureError as e:
        print(f"error due to: {e}")
        raise HTTPException(detail="invalid token", status_code= 403) 
    except Exception as e:
        print(f"error due to: {e}")
        raise HTTPException(detail="server error in decoding token", status_code= 500)
        