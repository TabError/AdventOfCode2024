# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
from typing import *

# =============== aocd ===============
from AOC import AOC

api = AOC(1, 2024, "github")
# api = AOC(1, 2024, "reddit")

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')

# =============== preparation ===============
data = api.input().splitlines()

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
    # api.submit_a(a)

    b = f2()
    print(b)
    # api.submit_b(b)

if __name__ == "__main__":
    main()

