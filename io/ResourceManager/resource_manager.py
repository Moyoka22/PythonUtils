from io import IOBase
from typing import Any, Dict, Union

from .errors import ResourceManagerError
from .resource_proxy import ResourceProxy


class ResourceManager:
    def __init__(self):
        self._resource_map: Dict[str, ResourceProxy] = {}

    def has(self, key: str) -> bool:
        return key in self._resource_map

    def get(self, key: str) -> Any:
        if not key in self._resource_map:
            raise ResourceManagerError.UndefinedResource(key=key)
        return self._resource_map.get(key).read()

    def define(self, key: str, loc: Union[str, IOBase]) -> None:
        if key in self._resource_map:
            raise ResourceManagerError.DuplicateKey(key=key)
        if not ResourceProxy._is_valid_loc(loc):
            raise ResourceManagerError.InvalidLocation()

        self._resource_map[key] = self._create_loc_io(loc)

    def save(self, key: str, data: Any) -> None:
        if not key in self._resource_map:
            raise ResourceManagerError.UndefinedResource(key=key)

        loc_io = self._resource_map[key]
        loc_io.write(data)

    def _create_loc_io(self, loc: Union[str, IOBase]) -> ResourceProxy:
        return ResourceProxy(loc)
