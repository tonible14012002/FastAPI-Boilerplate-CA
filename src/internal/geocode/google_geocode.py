from src.core import ports
from src.core import domain


class GoogleGeocodeService(ports.IGeocode):
    async def geocode(self, address) -> domain.Geocode:
        raise NotImplementedError("Google Geocoding API is not implemented yet.")