from src.core import services
from fastapi import FastAPI

class Entities:
    """
    Class holding the entities of the application.
    """

    def __init__(
            self,
            geocode_service: services.GeocodeService,
        ):
        """
        Initialize the entities.
        """
        self.geocode_service = geocode_service
        
    def include_to_app(self, app: FastAPI) -> FastAPI:
        """
        Include context to app instance.
        """
        app.entities = self
        return app