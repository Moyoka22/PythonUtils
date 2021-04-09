
import logging
from io import TextIOBase


class PrintLoggingInterceptor(TextIOBase):
    def write(self, s: str) -> int:
        logging.info(s, stacklevel=3)
        return len(s)
