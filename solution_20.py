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
handler: IOHandler = AOC(20, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j)

# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    data = data.splitlines()

    walls = { complex(j, i) for i, row in enumerate(data) for j, c in enumerate(row) if c == "#" }
    tracks = { complex(j, i) for i, row in enumerate(data) for j, c in enumerate(row) if c == "." }
    starts = { complex(j, i) for i, row in enumerate(data) for j, c in enumerate(row) if c == "S" }
    ends = { complex(j, i) for i, row in enumerate(data) for j, c in enumerate(row) if c == "E" }

    assert len(starts) == 1
    assert len(ends) == 1

    tracks |= starts | ends
    start = starts.pop()
    end = ends.pop()

    # =============== part a ===============
    def bfs() -> dict[complex, int]:
        dist = {}
        q = queue.Queue()

        q.put(end)
        dist[end] = 0
        while not q.empty():
            p = q.get()
            for d in dirs:
                n = p + d
                if n in tracks and n not in dist:
                    q.put(n)
                    dist[n] = dist[p] + 1

        return dist

    @ft.cache
    def poss_cheats(cheat_time: int) -> list[complex]:
        r = list(range(-cheat_time, cheat_time + 1))
        grid = it.product(r, repeat=2)

        # l = []
        # for i, j in grid:
        #     d = abs(i) + abs(j)
        #     if 2 <= d <= cheat_time:
        #         l.append((complex(i, j), d))
        # return l

        return [ (complex(i, j), d ) for i, j in grid if 2 <= (d := abs(i) + abs(j)) <= cheat_time ]

    def find_all_cheats(max_cheat_time: int) -> list[int]:
        dists = bfs()
        cheats = {}

        for cs in tracks:
            for co, l in poss_cheats(max_cheat_time):
                ce = cs + co
                if ce not in tracks:
                    continue
                saving = dists[cs] - dists[ce] - l
                if saving > 0:
                    cheats[(cs, ce)] = saving
        
        return cheats

    def part_a():
        return sum(c >= 100 for c in find_all_cheats(2).values())

    # =============== part b ===============
    def part_b():
        return sum(c >= 100 for c in find_all_cheats(20).values())

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

