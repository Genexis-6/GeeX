from app.config.env_config.dev_config import dev_config

REDIS_USERNAME = dev_config.REDIS_USERNAME
REDIS_PASSWORD = dev_config.REDIS_PASSWORD
REDIS_PORT = dev_config.REDIS_PORT
REDIS_HOST = dev_config.REDIS_HOST
REDIS_DECODE_RESPONSE = dev_config.REDIS_DECODE_RESPONSE


def build_redis_url():
    user_pass = ""
    if REDIS_USERNAME and REDIS_PASSWORD:
        user_pass = f"{REDIS_USERNAME}:{REDIS_PASSWORD}@"
    else:
        user_pass = f":{REDIS_PASSWORD}@"
    return f"redis://{user_pass}{REDIS_HOST}:{REDIS_PORT}"




