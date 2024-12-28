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
handler: IOHandler = AOC(21, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    data = data.splitlines()

    # =============== part a ===============
    numpad = {
            "0": -1,
            "A": -0,
            "1": -2 -1j,
            "2": -1 -1j,
            "3": -0 -1j,
            "4": -2 -2j,
            "5": -1 -2j,
            "6": -0 -2j,
            "7": -2 -3j,
            "8": -1 -3j,
            "9": -0 -3j,
            }
    numpad_gap = -2

    arrowpad = {
            "A": -0,
            "^": -1,
            "<": -2 + 1j,
            "v": -1 + 1j,
            ">": -0 + 1j,
            }
    arrowpad_gap = -2

    move = {
            "^": -1j,
            "v": 1j,
            "<": -1,
            ">": 1,
            "A": 0,
            }

    def way_is_fatal(way: str, pad: dict) -> bool:
        # assume this way starts at "A"
        moves = [ move[c] for c in way ]
        pos_ls = it.accumulate(moves, initial=pad["A"])
        return any(p not in pad.values() for p in pos_ls)


    def poss_transitions(d: complex) -> tuple[str]:
        v = ("v" if d.imag > 0 else "^") * int(abs(d.imag))
        h = (">" if d.real > 0 else "<") * int(abs(d.real))
        return tuple({v + h, h + v})
    

    @ft.cache
    def sequence_len_recursive(code: str, num_layers: int, depth: int = 0) -> int:
        if depth == num_layers:
            return len(code)

        # pad, gap = (arrowpad, arrowpad_gap) if depth else (numpad, numpad_gap) 
        pad = arrowpad if depth else numpad

        positions = [ pad[c] for c in "A" + code ]
        diffs = [ tar - cur for cur, tar in it.pairwise(positions) ]
        way_options = [ [ t + "A" for t in poss_transitions(d) ] for d in diffs ] 
        ways = list(it.product(*way_options))
        ways = [ w for w in ways if not way_is_fatal("".join(w), pad) ]
        lens = [ sum(sequence_len_recursive(part, num_layers, depth + 1) for part in way) for way in ways ]
        return min(lens)


    def part_a():
        return sum( sequence_len_recursive(code, num_layers = 2 + 1) * int(code[:-1]) for code in data )

    # =============== part b ===============
    def part_b():
        return sum( sequence_len_recursive(code, num_layers = 25 + 1) * int(code[:-1]) for code in data )

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

