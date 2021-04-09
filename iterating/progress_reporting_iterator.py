import logging
from typing import Iterable, Iterator


class ProgressReportingIterator(Iterator):
    def __init__(self, name, finite_iterable: Iterable,
                 length: int, report_increment_pct: float = 0.1,
                 stacklevel=4,
                 logging_level=logging.INFO):
        self.iterator = iter(finite_iterable)
        self._name = name
        self._total = length
        self._idx = 0
        self._report_increment_pct = report_increment_pct
        self._last_reported = 0
        self._stacklevel = stacklevel
        self._progress = 0
        self._logging_level = logging_level

    @property
    def progress(self):
        return self._progress

    def check_progress(self):
        progress = self._idx / self._total

        if (progress - self._last_reported) > self._report_increment_pct:
            logging.log(level=self._logging_level,
                        msg=f'{self._name} progress report: {progress*100:.2f}%.\n',
                        stacklevel=self._stacklevel)
            self._last_reported = progress
        self._progress = progress

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self._idx += 1
            nxt = next(self.iterator)
            self.check_progress()
        except StopIteration:
            self._idx = self._total
            self.check_progress()
            raise
        else:
            return nxt
