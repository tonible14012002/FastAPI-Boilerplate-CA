from src.core import ports
from typing import Optional

class RedisCache(ports.ICache):
    async def get(self, key) -> Optional[str]:
        # Implement the logic to get a value from Redis cache
        return None
    
    async def set(self, key, value):
        # Implement the logic to set a value in Redis cache
        pass

    async def delete(self, key):
        # Implement the logic to delete a value from Redis cache
        pass