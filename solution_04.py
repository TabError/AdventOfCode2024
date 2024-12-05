# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
from typing import *

# =============== aocd ===============
from Handler import IOHandler, StdIO, AOC

handler: IOHandler = AOC(4, 2024, "github", live=True)
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')

# =============== preparation ===============
data = handler.input().splitlines()

m, n = len(data), len(data[0])

# ll = [list(map(int, line.split())) for line in data]


# =============== part 1 ===============
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
check_coords = lambda i, j: 0 <= i < m and 0 <= j < n

word = "XMAS"
def check_word(i, j, di, dj):
    coords = [ (i + k * di, j + k * dj) for k in range(len(word)) ]
    if not all(check_coords(*c) for c in coords):
        return False
    oword = [ data[i][j] for i, j in coords ]
    return all(c == oc for c, oc in zip(word, oword))


def f1():
    res = 0
    for i in range(m):
        for j in range(n):
            for d in dirs:
                res += check_word(i, j, *d)
    return res

# =============== part 2 ===============
def check_xmas(i, j):
    if not data[i][j] == "A":
        return False
    if not check_coords(i - 1, j - 1) or not check_coords(i + 1, j + 1):
        return False
    return set("MS") == {data[i - 1][j - 1], data[i + 1][j + 1]} == {data[i - 1][j + 1], data[i + 1][j - 1]}

def f2():
    res = 0
    for i in range(m):
        for j in range(n):
            res += check_xmas(i, j)
    return res

# =============== main ===============
def main():
    a = f1()
    handler.submit_a(a)

    b = f2()
    handler.submit_b(b)


    import datetime as dt
    print(dt.datetime.now().strftime("%T:%f")[:-3])
    print()


if __name__ == "__main__":
    main()

