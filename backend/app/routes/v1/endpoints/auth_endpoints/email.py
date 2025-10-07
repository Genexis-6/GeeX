from fastapi import APIRouter


email = APIRouter(
    prefix="/email",
    responses={
        404: {
            "message":"not found"
        }
    },
    tags=["emails"]
)


@email.get("/verify")
async def verify_email():
    return "working"