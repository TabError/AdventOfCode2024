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
handler: IOHandler = AOC(23, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    data = data.splitlines()
    edges = [ line.split("-") for line in data ]

    adj = col.defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # =============== part a ===============
    def bigger_cliques(cliques: set[frozenset]):
        bigger = set()
        feasible_nodes = { u for cl in cliques for u in cl }
        for c in cliques:
            for n in feasible_nodes:
                if all(n in adj[u] for u in c):
                    l = list(c) + [n]
                    bigger.add(frozenset(l))
        return bigger

    cliques: dict[int, set[frozenset]] = dict()
    cliques[1] = {frozenset([u]) for u in adj}

    def find_cliques(size: int, check_t: bool = False, info: bool = False):
        assert size >= 1
        if size in cliques:
            return cliques[size]

        cs = find_cliques(size - 1, check_t)
        if info:
            print("exploring cliques of size", size)
        cliques[size] = bigger_cliques(cs)
        return cliques[size]

    def part_a():
        cs = find_cliques(3, check_t=True)
        res = sum(any(u.startswith("t") for u in c) for c in cs)
        return res

    # =============== part b ===============
    def part_b():
        k = 1
        while find_cliques(k + 1):
            k += 1

        max_cliques = find_cliques(k)
        assert len(max_cliques) == 1

        sol = max_cliques.pop()
        sol = sorted(list(sol))
        res = ",".join(sol)
        return res

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

