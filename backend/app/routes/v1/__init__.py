from fastapi import APIRouter
from .endpoints.auth_endpoints.auth import auth
from .endpoints.auth_endpoints.email import email


v1_api = APIRouter(prefix="/v1", responses= {404:{"message":"not found"}}, tags=["v1"])


# authentication endpoint
v1_api.include_router(auth)
v1_api.include_router(email)