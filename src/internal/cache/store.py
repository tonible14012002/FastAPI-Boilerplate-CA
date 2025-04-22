from src.core import ports


class CacheStore(ports.ICacheStore):
    def __init__(self, cache: ports.ICache):
        self._cache = cache
        super().__init__()

    async def get_geocode(self, key):
        await self._cache.get(key)
        # ...

    async def set_geocode(self, key, value):
        await self._cache.set(key, value)
        # ...