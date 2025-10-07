from fastapi import FastAPI, HTTPException
import contextlib
from app.middleware.CORS.cors_middleware import setup_cors
from app.repo import db_session_manager
from app.routes import all_routes
from app.security.exceptions.api_res_exceptions import custom_http_exception_handler





@contextlib.asynccontextmanager
async def lifespan(app):
    await db_session_manager.start()
    yield
    await db_session_manager.end()
    
    
    

app = FastAPI(
    title="payment wrapper", lifespan=lifespan,
)

setup_cors(app=app)


@app.get("/")
async def welcome():
    return "api running"


all_routes(app=app)



# a custom global exception handler
app.add_exception_handler(HTTPException, custom_http_exception_handler)

