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

api = AOC(3, 2024, "github")

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')

# =============== preparation ===============
data = api.input().splitlines()
# data = open(0).read().splitlines()

# ll = [list(map(int, line.split())) for line in data]


# =============== part 1 ===============
def f1():
    pat = r"mul\((\d+),(\d+)\)"
    p = re.compile(pat)

    res = 0
    for l in data:
        ls = p.findall(l)
        ls = [ (int(a), int(b)) for a, b in ls ]
        res += sum(a * b for a, b in ls)

    return res


# =============== part 2 ===============
def f2():
    pat = r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))"
    p = re.compile(pat)

    res = 0
    enable = True
    for l in data:
        ls = p.findall(l)

        for item in ls:
            if item[3]: # do()
                enable = True
            elif item[4]: # don't()
                enable = False
            else:
                if enable:
                    res += int(item[1]) * int(item[2])

    return res

# =============== main ===============
def main():
    a = f1()
    print(a)
    api.submit_a(a)

    b = f2()
    print(b)
    api.submit_b(b)


    import datetime as dt
    print(dt.datetime.now().strftime("%T:%f")[:-3])


if __name__ == "__main__":
    main()

