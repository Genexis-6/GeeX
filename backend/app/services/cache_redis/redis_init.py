from redis.asyncio import Redis
from app.utils.helpers.build_redis_url import build_redis_url, REDIS_DECODE_RESPONSE


redis = None

async def get_redis_client():
    global redis
    if redis is None:
        redis_url = build_redis_url()
        redis = await Redis.from_url(
            redis_url,
            encoding="utf-8",
            decode_responses=REDIS_DECODE_RESPONSE
        )
    return redis





