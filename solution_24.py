# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
import bisect

from graphlib import TopologicalSorter, CycleError
from operator import and_, or_, xor as xor_

# =============== handler ===============
from Handler import IOHandler, StdIO, AOC

live = 0
handler: IOHandler = AOC(24, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    init, config = data.split("\n\n")

    init = [ line.split(": ") for line in init.splitlines() ]
    init = { node: val == "1" for node, val in init }

    config = [ line.split(" -> ") for line in config.splitlines() ]
    config = { target: desc.split() for desc, target in config }

    # =============== part a ===============
    check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

    def top_sort(config) -> list:
        T = TopologicalSorter()
        for t, (u, _, v) in config.items():
            T.add(t, u, v)
        try:
            r = list(T.static_order())
        except CycleError:
            r = None
        return r

    def simulate(init, config) -> int:
        # init
        status = col.defaultdict(bool, init)

        # sort nodes
        sorted_nodes = top_sort(config)
        if sorted_nodes is None:
            return None

        # run all nodes
        for node in sorted_nodes:
            if node not in config:
                continue
            u, o, v = config[node]
            hack = f"{o.lower()}_({status[u]}, {status[v]})"
            status[node] = bool(eval(hack))

        # extract values from z wires
        zs = [ node for node in status if node.startswith("z") ]
        zs.sort(reverse=True)
        res = "".join("1" if status[z] else "0" for z in zs)
        res = int(res, 2)
        return res

    def part_a():
        res = simulate(init, config)
        return res

    # =============== part b ===============
    def wire_check(c: str) -> int:
        vals = { int(node[1:]) for node in it.chain(init, config) if node.startswith(c) }
        assert vals == set(range(len(vals)))
        return len(vals)

    nums_x = wire_check("x")
    nums_y = wire_check("y")
    nums_z = wire_check("z")

    assert nums_x == nums_y
    # print(nums_x, nums_z)
    assert nums_x + 1 == nums_z


    def tests_for_bit(n: int):
        # n - zero based index
        val = 2 ** n
        return [ (val // 2, val // 2), (val, 0), (0, val) ]

    def test_gen(num_bits: int = nums_x):
        return [ t for i in range(num_bits) for t in tests_for_bit(i) ]


    int_to_bin = lambda x: list(reversed(bin(x)[2:]))

    def make_init(x: int, y: int) -> dict:
        init = {}
        for i, c in enumerate(int_to_bin(x)):
            init[f"x{i:02}"] = c == "1"
        for i, c in enumerate(int_to_bin(y)):
            init[f"y{i:02}"] = c == "1"
        return init


    def swappable_nodes(config, node):
        sorted_nodes = top_sort(config)
        sorted_nodes = [ n for n in sorted_nodes if n in config ]

        r = range(len(sorted_nodes))
        idx = sorted_nodes.index(node)
        offset = 1
        ls = []
        while idx - offset in r or idx + offset in r:
            if idx - offset in r:
                ls.append(sorted_nodes[idx - offset])
            if idx + offset in r:
                ls.append(sorted_nodes[idx + offset])
            offset += 1
        # assert len(ls) == len(r) - 1
        return ls

    def poss_swaps(config: dict, node: str):
        assert node in config
        ls = [ node ]

        i = 0
        while i < len(ls):
            u, _, v = config[ls[i]]
            if u in config: ls.append(u)
            if v in config: ls.append(v)

            for o in swappable_nodes(config, ls[i]):
                if o not in ls[:i]:
                    yield ls[i], o
            i += 1

    def analyze(x: int, y: int, config: dict) -> bool:
        init = make_init(x, y)
        sim_z = simulate(init, config)
        return sim_z == x + y

    def suite(tests: list[tuple], config) -> bool:
        for t in tests:
            if not analyze(*t, config):
                return False
        return True

    def part_b():
        swaps = []

        c = config.copy()
        for i in range(nums_x):
            if not suite(tests_for_bit(i), c):
                node = f"z{i:02}"
                # print(f"fix", node)
                for a, b in poss_swaps(c, node):
                    c[a], c[b] = c[b], c[a]
                    if suite(reversed(test_gen(i + 2)), c):
                        # print(f"success fixed {i:02}")
                        # print(f"=== {a} - {b} ===")
                        swaps.append(a)
                        swaps.append(b)
                        break
                    c[a], c[b] = c[b], c[a]
                else:
                    print("can't fix error")

        return ",".join(sorted(swaps))

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

