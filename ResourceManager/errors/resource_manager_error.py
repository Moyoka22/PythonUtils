from __future__ import annotations


class ResourceManagerError(Exception):

    @classmethod
    def DuplicateKey(cls, key: str) -> ResourceManagerError:
        return cls(f"Cannot define key '{key}' since key already exists.")

    @classmethod
    def InvalidLocation(cls):
        return cls("Invalid location supplied. Locations must be a valid url or buffer.")

    @classmethod
    def UndefinedResource(cls, key: str) -> ResourceManagerError:
        return cls(f"Resource '{key}' not defined.")

    @classmethod
    def UnsupportedProtocol(cls, url: str) -> ResourceManagerError:
        return cls(f"Url type '{url}' is not a supported.")
