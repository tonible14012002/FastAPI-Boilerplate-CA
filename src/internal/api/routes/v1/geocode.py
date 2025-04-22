from src.internal.api.routes.base import BaseAPIRouter
from src.core import domain

class GeocodeAPIRouter(BaseAPIRouter):
    pass

router = GeocodeAPIRouter(
    tags=["v1-geocode"],
)


@router.post(
    "/search",
    status_code=200,
    response_model=domain.Geocode,
)
async def geocode(
    address: str,
):
    """
    Geocode an address.
    """
    # Get the geocode from the cache
    location = router.entities.geocode_service.get_location(address=address)
    return location