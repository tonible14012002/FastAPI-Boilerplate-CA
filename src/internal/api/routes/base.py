from fastapi import APIRouter
from fastapi.requests import Request
from src.internal.entities import Entities

class BaseAPIRouter(APIRouter):
    """
    Inherit this class for accessing entities.
    """
    @property
    def entities(self, request: Request) -> Entities:
        return request.app.entities