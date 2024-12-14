# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
from typing import *
import bisect

from time import sleep

# =============== handler ===============
from Handler import IOHandler, StdIO, AOC

live = 1
handler: IOHandler = AOC(14, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    data = data.splitlines()
    pat = r"\Ap=(.*?),(.*?) v=(.*?),(.*?)\Z"
    pat = re.compile(pat)
    data = [ pat.match(line).groups() for line in data ]
    data = [ [ int(v) for v in g ] for g in data ]
    data = [ (complex(px, py), complex(vx, vy)) for px, py, vx, vy in data ]

    m, n = 103, 101

    # =============== part a ===============
    check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

    def simulate_moves(bots: list, steps: int = 100):
        for _ in range(steps):
            newbots = []
            for bot, speed in bots:
                bot += speed
                bot = complex(bot.real % n, bot.imag % m)
                newbots.append((bot, speed))
            bots = newbots
        return bots


    def part_a():
        bots = simulate_moves(data.copy(), 100)

        a, b, c, d = 0, 0, 0, 0
        mn, mm = n // 2, m // 2
        for bot, _ in bots:
            if bot.real < mn:
                if bot.imag < mm:
                    a += 1
                if bot.imag > mm:
                    b += 1
            if bot.real > mn:
                if bot.imag < mm:
                    c += 1
                if bot.imag > mm:
                    d += 1
        return prod([a, b, c, d])

    # =============== part b ===============
    def show_them(bots: list):
        grid = [ [0] * n for _ in range(m) ]
        for b, _ in bots:
            grid[int(b.imag)][int(b.real)] += 1

        pic = [ [ '#' if v else ' ' for v in row ] for row in grid ]
        for row in pic:
            print("".join(row))

    def num_components(bots: list) -> int:
        bots = { pos for pos, _ in bots }
        num = 0

        while bots:
            stack = [ bots.pop() ]
            comp = set(stack)
            num += 1
            while stack:
                b = stack.pop()
                for d in dirs:
                    n = b + d
                    if n in bots and n not in comp:
                        stack.append(n)
                        comp.add(n)
            bots -= comp
        return num

    def part_b():
        bots = data.copy()

        ls = []
        for i in it.count(1):
            bots = simulate_moves(bots, 1)
            # print(f"step {i} {90 * '='}")
            # show_them(bots)
            # sleep(0.5)
            if num_components(bots) < 200:
                # show_them(bots)
                return i


    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

