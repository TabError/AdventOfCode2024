# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
from typing import *

# =============== aocd ===============
from aocd import get_puzzle, submit
from aocd.models import _load_users

year, day = 2024, 0
user = "github"
# user = "reddit"
aocd_session = _load_users()[user]

puzzle = get_puzzle(year=year, day=day, session=aocd_session)

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')

# =============== preparation ===============
data = puzzle.input_data.splitlines()

# =============== part 1 ===============
def f1():
    pass

# =============== part 2 ===============
def f2():
    pass

# =============== main ===============
def main():
    a = f1()
    print(a)
    # submit(a, part="a", session=aocd_session)

    b = f2()
    print(b)
    # submit(b, part="b", session=aocd_session)

if __name__ == "__main__":
    main()

