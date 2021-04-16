
from .manager import ProtocolManager, FileManager
from .tester import ProtocolTester, FileTester


class ResourceProtocolSpecification:
    def __init__(self, tester: ProtocolTester,
                 manager: ProtocolManager):
        self.tester = tester
        self.manager = manager


SUPPORTED_PROTOCOLS = [
    ResourceProtocolSpecification(tester=FileTester,
                                  manager=FileManager)
]
