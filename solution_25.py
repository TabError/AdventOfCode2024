# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
import bisect

# =============== handler ===============
from Handler import IOHandler, StdIO, AOC

live = 1
handler: IOHandler = AOC(25, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    data = [ schema.splitlines() for schema in data.split("\n\n") ]

    keys, locks = [], []
    for schema in data:
        schema = list(zip(*schema)) # transpose
        lok = [line.count("#") for line in schema]
        lok = tuple(lok)
        if schema[0][0] == "#": # lock
            locks.append(lok)
        else: # key
            keys.append(lok)

    # =============== part a ===============
    def key_lock_match(key: tuple[int], lock: tuple[int]) -> bool:
        return all(k + l <= 7 for k, l in zip(key, lock))

    def part_a():
        return sum(key_lock_match(k, l) for k, l in it.product(keys, locks))

    # =============== part b ===============
    def part_b():
        res = 0

        return res

    # =============== print ===============
    handler.submit_a(part_a())
    # handler.submit_b(part_b())


if __name__ == "__main__":
    main()

