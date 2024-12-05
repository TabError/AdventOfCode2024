# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
from typing import *

# =============== handler ===============
from Handler import IOHandler, StdIO, AOC

handler: IOHandler = AOC(5, 2024, "github", live=bool(0))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')

# =============== preparation ===============
data = handler.input()

rules, samples = data.split("\n\n")
rules = [list(map(int, line.split("|"))) for line in rules.strip().splitlines()]
samples = [list(map(int, line.split(","))) for line in samples.strip().splitlines()]

# # this is huge ...
# for s in samples:
#     for a, b in it.combinations(s, r=2):
#         b = [a,b] in rules or [b,a] in rules
#         if not b:
#             print("Problem:",a,b)

# =============== part 1 ===============
def correct(ls) -> bool:
    n = len(ls)
    for i in range(n):
        for j in range(i + 1, n):
            if [ls[i], ls[j]] not in rules:
                return False
    return True

def f1():
    res = 0
    for update in samples:
        if correct(update):
            res += update[len(update) // 2]
    return res

# =============== part 2 ===============
def get_correct(ls) -> list:
    nls = [0] * len(ls)
    for e in ls:
        c = sum([o, e] in rules for o in ls)
        nls[c] = e
    return nls

def f2():
    res = 0
    for update in samples:
        if not correct(update):
            nup = get_correct(update)
            res += nup[len(nup) // 2]
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

