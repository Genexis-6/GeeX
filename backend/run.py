import uvicorn
from app.config.env_config.dev_config import dev_config


if __name__ == "__main__":
    uvicorn.run(
        app=dev_config.APP_NAME,
        host=dev_config.HOST,
        reload=dev_config.DEBUG,
        port=dev_config.PORT,
    )