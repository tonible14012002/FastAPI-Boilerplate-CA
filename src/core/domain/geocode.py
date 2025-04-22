from pydantic import BaseModel, Field

__all__ = ["Geocode"]

class Geocode(BaseModel):
    """
    Geocode model for storing geocoding information.
    """
    latitude: float = Field(..., description="Latitude of the location")
    longitude: float = Field(..., description="Longitude of the location")
    address: str = Field(..., description="Formatted address of the location")
    city: str = Field(..., description="City of the location")
    state: str = Field(..., description="State of the location")
    country: str = Field(..., description="Country of the location")
    geocoe: str = Field(..., description="Geocode of the location")