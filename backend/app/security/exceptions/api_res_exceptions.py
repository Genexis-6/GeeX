from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import HTTPException


async def custom_http_exception_handler(requst: Request, exc:HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code":exc.status_code,
            "message":exc.detail
        }
    )