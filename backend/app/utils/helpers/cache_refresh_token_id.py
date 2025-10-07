from app.services.cache_redis.redis_init import get_redis_client
from ..enums.auth_enums import AuthEnums
import requests

async def cache_session_token_id(token: str,id):   
    try:
        redis = await get_redis_client()
        await redis.setex(
            name=f"session_id:{id}",
            value=token,
            time= 604800
        )
        await redis.close()
    except requests.exceptions.ConnectionError as e:
        return AuthEnums.ERROR
    
    except Exception as e:
        print(f"error due to: {e}")


async def get_cache_refresh_token(token_id: str):
    try:
        redis = await get_redis_client()
        id:str = await redis.get(f"session_id:{token_id}")
        return id
    except requests.exceptions.ConnectionError as e:
        return AuthEnums.ERROR
    
    except Exception as e:
        print(f"error getting token due to: {e}")
        return AuthEnums.FAILED