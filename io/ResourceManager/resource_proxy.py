from io import IOBase
from typing import Any, Union

from .errors.resource_manager_error import ResourceManagerError

from .protocols import SUPPORTED_PROTOCOLS


class ResourceProxy:
    def __init__(self, loc: Union[str, IOBase]):
        if issubclass(type(loc), IOBase):
            self._manager = IOWrapper(loc)
            return
        else:
            for protocol in SUPPORTED_PROTOCOLS:
                tester = protocol.tester()
                if tester(loc):
                    self._manager = protocol.manager(loc)
                    return

        raise ResourceManagerError.UnsupportedProtocol()

    def write(self, data: Any):
        ...

    def read(self):
        ...

    @staticmethod
    def _is_valid_loc(loc: Union[str, IOBase]) -> bool:
        ...
