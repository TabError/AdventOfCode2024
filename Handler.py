from abc import ABC, abstractmethod
from time import time as now, sleep

from aocd import get_puzzle, submit
from aocd.models import _load_users



class IOHandler(ABC):
    @abstractmethod
    def input(self) -> str:
        ...
    @abstractmethod
    def submit_a(self, value) -> None:
        ...
    @abstractmethod
    def submit_b(self, value) -> None:
        ...


class StdIO(IOHandler):
    def input(self):
        return open(0).read()

    def submit_a(self, value):
        print(value)

    def submit_b(self, value):
        print(value)


AOC_REQUEST_DELAY = 0.2 # used as seconds

class AOC(IOHandler):
    def __init__(self, day: int, year: int, user: str, live: bool):
        self.day = day
        self.year = year
        self.user = user
        self.live = live

        self.session = _load_users()[self.user]

        self.puzzle = get_puzzle(
            year=self.year,
            day=self.day,
            session=self.session,
        )
        self._last_request = now()

    def input(self) -> str:
        return self.puzzle.input_data

    def _submit_part(self, value, part) -> None:
        if self._last_request >= now() - AOC_REQUEST_DELAY:
            sleep(AOC_REQUEST_DELAY)
        submit(value, part=part, day=self.day, year=self.year, session=self.session)
        self._last_request = now()

    def submit_a(self, value) -> None:
        print(value)
        if self.live:
            self._submit_part(value, "a")

    def submit_b(self, value) -> None:
        print(value)
        if self.live:
            self._submit_part(value, "b")


