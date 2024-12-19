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
handler: IOHandler = AOC(16, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    data = data.splitlines()
    walls = { complex(j, i) for i, row in enumerate(data) for j, c in enumerate(row) if c == "#" }
    spots = { complex(j, i) for i, row in enumerate(data) for j, c in enumerate(row) if c == "." }
    starts = { complex(j, i) for i, row in enumerate(data) for j, c in enumerate(row) if c == "S" }
    ends = { complex(j, i) for i, row in enumerate(data) for j, c in enumerate(row) if c == "E" }
    assert len(starts) == 1
    assert len(ends) == 1

    def adj(p: complex, v: complex) -> list[tuple[complex, complex]]:
        return [
                (1, (p + v, v)),
                (1000, (p, v * 1j)),
                (1000, (p, v * -1j)),
                ]

    def dijkstra(start, startview) -> dict[complex, int]:
        call = lambda: 1e12
        scores = col.defaultdict(call)

        gen = it.count()

        t = start, startview
        scores[t] = 0
        q = queue.PriorityQueue()
        q.put((scores[t], next(gen), t))

        while not q.empty():
            ps, _, p = q.get()
            if scores[p] < ps:
                continue

            for ds, n in adj(*p):
                ns = ps + ds
                if n[0] not in walls and ns < scores[n]:
                    scores[n] = ns
                    q.put((ns, next(gen), n))

        return scores

    start = starts.copy().pop()
    startview = 1
    end = ends.copy().pop()

    scores = dijkstra(start, startview)
    assert len(scores) == (len(spots) + len(starts) + len(ends)) * 4

    # =============== part a ===============
    check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

    def part_a():
        res = min(v for (p, _), v in scores.items() if end == p)
        return res

    # =============== part b ===============
    def pre_adj(p: complex, v: complex) -> list[tuple[complex, complex]]:
        return [
                (1, (p - v, v)),
                (1000, (p, v * -1j)),
                (1000, (p, v * 1j)),
                ]

    def part_b():
        end_keys = [ (end, 1j ** k) for k in range(4) ]
        sol = min(end_keys, key=lambda k: scores[k])

        tiles = {sol}
        ls = [sol]
        while ls:
            p = ls.pop()
            for ds, n in pre_adj(*p):
                if scores[n] == scores[p] - ds:
                    tiles.add(n)
                    ls.append(n)

        tiles = { p for p, _ in tiles }
        res = len(tiles)

        return res

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

