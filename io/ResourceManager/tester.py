from abc import abstractmethod, ABC


class ProtocolTester(ABC):

    def __call__(self, *args, **kwargs):
        self.test(*args, **kwargs)

    @abstractmethod
    def test(self, url: str) -> bool:
        ...


class FileTester(ProtocolTester):

    def test(self, url: str) -> bool:
        return False
