from abc import ABC, abstractmethod

__all__ = [
    "ICache",
    "ICacheStore",
]

class ICache(ABC):
    """
    Interface for cache operations.
    """

    @abstractmethod
    async def get(self, key: str) -> str:
        """
        Get a value from the cache by key.
        """
        raise NotImplementedError

    @abstractmethod
    async def set(self, key: str, value: str) -> None:
        """
        Set a value in the cache with a key.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete(self, key: str) -> None:
        """
        Delete a value from the cache by key.
        """
        raise NotImplementedError

class ICacheStore(ABC):
    """
    Interface for geocode cache operations.
    """

    @abstractmethod
    async def get_geocode(self, key: str) -> str:
        """
        Get a geocode from the cache by key.
        """
        raise NotImplementedError
    
    @abstractmethod
    async def set_geocode(self, key: str, value: str) -> None:
        """
        Set a geocode in the cache with a key.
        """
        raise NotImplementedError
    
    # NOTE: Add domain specific Cache Methods ...
