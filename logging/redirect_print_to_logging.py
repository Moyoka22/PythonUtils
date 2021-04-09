import sys
from contextlib import contextmanager

from .PrintLoggingInterceptor import PrintLoggingInterceptor


@contextmanager
def redirect_print_to_logging():
    redirect_io = PrintLoggingInterceptor()
    try:
        sys.stdout = redirect_io
        yield
    finally:
        sys.stdout = sys.__stdout__
