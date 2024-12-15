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
handler: IOHandler = AOC(15, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    wh, moves = data.split("\n\n")

    # moves
    mt = {
            "<": -1,
            ">": 1,
            "v": 1j,
            "^": -1j,
            }
    moves = [ mt[e] for line in moves.splitlines() for e in line ]

    # warehouse
    wh = wh.splitlines()
    boxes = { complex(j, i) for i, row in enumerate(wh) for j, e in enumerate(row) if e == "O" }
    walls = { complex(j, i) for i, row in enumerate(wh) for j, e in enumerate(row) if e == "#" }
    bots = { complex(j, i) for i, row in enumerate(wh) for j, e in enumerate(row) if e == "@" }
    assert len(bots) == 1


    # warehouse 2
    wht = { "#": "##", ".":"..", "@":"@.", "O":"[]" }
    wh2 = [ [wht[e] for e in line ] for line in wh ]
    wh2 = [ "".join(line) for line in wh2 ]

    walls2 = { complex(j, i) for i, row in enumerate(wh2) for j, e in enumerate(row) if e == "#" }
    lboxes = { complex(j, i) for i, row in enumerate(wh2) for j, e in enumerate(row) if e == "[" }
    rboxes = { complex(j, i) for i, row in enumerate(wh2) for j, e in enumerate(row) if e == "]" }
    boxes2 = lboxes | rboxes
    bots2 = { complex(j, i) for i, row in enumerate(wh2) for j, e in enumerate(row) if e == "@" }
    assert len(bots2) == 1


    # =============== part a ===============
    check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

    def solve_box(p, m):
        if p in walls:
            return False
        if p not in boxes:
            return p

        return solve_box(p + m, m)

    def part_a():
        bot = bots.pop()
        for m in moves:
            if bot + m in walls:
                continue
            elif bot + m in boxes:
                r = solve_box(bot + m, m)
                if isinstance(r, complex):
                    bot += m
                    boxes.add(r)
                    boxes.remove(bot)
            else:
                bot += m

        res = sum(b.real + b.imag * 100 for b in boxes)
        return int(res)

    # =============== part b ===============
    def solve_hori(p, m, exe: bool = False):
        if p in walls2:
            return False
        if p not in boxes2:
            return True
        
        # p is in boxes2
        if solve_hori(p + m, m, exe):
            if exe:
                assert p + m not in boxes2
                boxes2.remove(p)
                boxes2.add(p + m)
                if p in lboxes:
                    lboxes.remove(p)
                    lboxes.add(p + m)
                else:
                    rboxes.remove(p)
                    rboxes.add(p + m)
            return True
        else:
            assert not exe
            return False

    def solve_vert(p, m, exe: bool = False):
        if p in walls2:
            return False
        if p not in boxes2:
            return True
        
        # p is in boxes2
        if p in lboxes:
            l, r = p, p + 1
        else:
            l, r = p - 1, p

        assert l in lboxes
        assert r in rboxes

        resl = solve_vert(l + m, m, exe)
        resr = solve_vert(r + m, m, exe)

        if resl and resr:
            if exe:
                boxes2.remove(l)
                boxes2.add(l + m)
                lboxes.remove(l)
                lboxes.add(l + m)
                boxes2.remove(r)
                boxes2.add(r + m)
                rboxes.remove(r)
                rboxes.add(r + m)
            return True
        else:
            assert not exe
            return False

    def show():
        m = [ ['.'] * len(wh2[0]) for line in wh2 ]
        for b in boxes2:
            i, j = int(b.imag), int(b.real)
            m[i][j] = "x"
        for b in walls2:
            i, j = int(b.imag), int(b.real)
            m[i][j] = "#"

        for l in m:
            print("".join(l))

    def part_b():
        bot = bots2.pop()
        for m in moves:
            assert boxes2 == lboxes | rboxes
            assert len(boxes2) == len(lboxes) + len(rboxes)
            if bot + m in walls2:
                continue
            elif bot + m in boxes2:
                if m.imag == 0: # horizontal move
                    if solve_hori(bot + m, m):
                        solve_hori(bot + m, m, exe=True)
                        bot += m
                else: # vertical move
                    if solve_vert(bot + m, m):
                        solve_vert(bot + m, m, exe=True)
                        bot += m
            else:
                bot += m
        
        # show()
               
        res = sum(b.real + b.imag * 100 for b in lboxes)
        return int(res)

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

