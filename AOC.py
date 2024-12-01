from aocd import get_puzzle, submit
from aocd.models import _load_users


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

    def input(self) -> str:
        return self.puzzle.input_data

    def submit_a(self, value) -> None:
        submit(value, part="a", session=self.session)

    def submit_b(self, value) -> None:
        submit(value, part="b", session=self.session)

