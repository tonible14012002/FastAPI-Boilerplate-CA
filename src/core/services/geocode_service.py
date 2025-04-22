from src.core import ports
from src.core import domain

class GeocodeService:
    def __init__(
            self,
            geocoder: ports.IGeocode,
            cache_store: ports.ICacheStore # Empty cache store
        ):
        assert geocoder is not None, "Geocoder cannot be None"
        self._geocoder = geocoder
        self._cache_store = cache_store

    async def get_location(self, address) -> domain.Geocode:
        try:
            location = await self._geocoder.geocode(address)
            return location
        except Exception as e:
            print(f"Error geocoding address {address}: {e}")
            raise