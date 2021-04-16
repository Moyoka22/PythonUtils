from abc import abstractmethod, ABC


class ProtocolManager(ABC):
    def __init__(self, url):
        ...


class FileResolver(ProtocolManager):
    pass
