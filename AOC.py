from aocd import get_puzzle, submit
from aocd.models import _load_users

from time import time as now, sleep

REQUEST_DELAY = 0.2 # used as seconds

class AOC():
    def __init__(self, day: int, year: int, user: str):
        self.day = day
        self.year = year
        self.user = user

        self._setup()

    def _setup(self) -> None:
        self.session = _load_users()[self.user]

        self.puzzle = get_puzzle(
            year=self.year,
            day=self.day,
            session=self.session,
        )
        self._last_request = now()

    def input(self) -> str:
        return self.puzzle.input_data

    def submit_a(self, value) -> None:
        if self._last_request >= now() - REQUEST_DELAY:
            sleep(REQUEST_DELAY)
        submit(value, part="a", day=self.day, year=self.year, session=self.session)
        self._last_request = now()

    def submit_b(self, value) -> None:
        if self._last_request >= now() - REQUEST_DELAY:
            sleep(REQUEST_DELAY)
        submit(value, part="b", day=self.day, year=self.year, session=self.session)
        self._last_request = now()

