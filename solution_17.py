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
handler: IOHandler = AOC(17, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    data = data.split("\n\n")
    # ll = [list(map(int, line.split())) for line in data]
    # m, n = len(data), len(data[0])

    pat = r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)"
    m = re.match(pat, data[0])
    A,B,C = map(int, m.groups())
    program = data[1].split(":")[1]
    program = [ int(op) for op in program.strip().split(",") ]


    # =============== part a ===============
    check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

    def combo_op(val, A, B, C):
        match val:
            case 4:
                operand = A
            case 5:
                operand = B
            case 6:
                operand = C
            case 7:
                raise ValueError("operand is 7")
            case _:
                operand = val
        return operand

    def one_instruction(A, B, C, instr, operand):
        o = None
        match instr:
            case 0:
                operand = combo_op(operand, A, B, C)
                A = A // (2 ** operand)
            case 1:
                # operand is literal
                B ^= operand
            case 2:
                operand = combo_op(operand, A, B, C)
                B = operand % 8
            case 3:
                raise ValueError
                # # operand is literal
                # if A != 0:
                #     instr = operand
                #     continue
            case 4:
                # ignores operand
                B ^= C
            case 5:
                operand = combo_op(operand, A, B, C)
                # outputs.append(operand % 8)
                o = operand % 8
            case 6:
                operand = combo_op(operand, A, B, C)
                B = A // (2 ** operand)
            case 7:
                operand = combo_op(operand, A, B, C)
                C = A // (2 ** operand)
        return A, B, C, o


    def sim(A, B, C):
        outputs = []
        pointer = 0

        while pointer < len(program):
            instr = program[pointer]
            operand = program[pointer + 1]

            if instr == 3:
                if A:
                    # operand is literal
                    pointer = operand
                else:
                    pointer += 2
            else:
                A, B, C, o = one_instruction(A, B, C, instr, operand)
                if o is not None:
                    outputs.append(o)
                pointer += 2

        return outputs

    def part_a():
        outs = sim(A, B, C)
        res = ",".join(map(str, outs))
        return res

    # =============== part b ===============
    def my_program_cycle(A) -> int:
        # 2, 4
        B = A % 8
        # 1, 2
        B ^= 2
        # 7, 5
        C = A // (2 ** B)
        # 4, 5
        B ^= C
        # 1, 3
        B ^= 3
        # 5, 5
        output = B % 8
        # 0, 3
        # A //= 8
        # 3, 0
        # do it again
        # ... unless A is zero
        return output

    def sim2(A, check: bool = False):
        outputs = []

        while A:
            o = my_program_cycle(A)
            # o = one_cycle(A)
            A >>= 3 # A //= 8
            outputs.append(o)

            if check and len(outputs) > 0:
                i = len(outputs) - 1
                if outputs[i] != program[i]:
                    return False

        return outputs

    def ultimate_simulater() -> int:
        # ultimate simulater
        for i in it.count(1):
            if i % 1_000_000 == 0:
                print(f"checking {i}'s ...")
            outs = sim2(i, check=True)
            if outs == program:
                return i



    # cyc = [(2, 4), (1, 2), (7, 5), (4, 5), (1, 3), (5, 5), (0, 3), (3, 0)]
    cyc = list(zip(program[::2], program[1::2]))

    def check_cycle():
        instrs = [ i for i, _ in cyc ]

        # if all these asserts are fulfilled,
        # this program should compute the solution
        assert 2 in instrs # to overwrite B
        assert 7 in instrs # to overwrite C
        assert 5 in instrs # to output something
        assert 0 in instrs # to cut the last 3 bits of A
        assert instrs[-1] == 3 # last instructions is supposed to be jump

    def one_cycle(A) -> int: # replacement for my_program_cycle
        B, C = 0, 0
        for t in cyc:
            A, B, C, o = one_instruction(A, B, C, *t)
            if o is not None:
                return o

    def find_rec(A, ls: list[int]):
        if not ls:
            return A
        o = ls[-1]
        A <<= 3
        for i in range(8):
            if o == one_cycle(A + i):
                oA = find_rec(A + i, ls[:-1])
                if oA:
                    return oA
        else:
            return False

    def part_b():
        # return ultimate_simulater()

        # solution
        res = find_rec(0, program)
        outs = sim(res, 0, 0)
        assert outs == program

        return res


    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

