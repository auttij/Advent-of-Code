from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


A = 51342988
B = 0
C = 0
ip = 0
P = list(map(int, "2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0".split(",")))


def combo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 3
    if x == 4:
        return A
    if x == 5:
        return B
    if x == 6:
        return C
    return None


def step():
    global A, B, C, P, ip
    instr = P[ip]
    opcode = P[ip + 1]
    ip += 2
    if instr == 0:
        A = A // (2 ** combo(opcode))
    if instr == 1:
        B = B ^ opcode
    if instr == 2:
        B = combo(opcode) % 8
    if instr == 3:
        if A != 0:
            ip = opcode
    if instr == 4:
        B = B ^ C
    if instr == 5:
        return combo(opcode) % 8
    if instr == 6:
        B = A // (2 ** combo(opcode))
    if instr == 7:
        C = A // (2 ** combo(opcode))


def run(a):
    global A, B, C, P, ip
    ip = 0
    A = a
    B = 0
    C = 0
    result = []
    while ip < len(P):
        out = step()
        if out is not None:
            result.append(out)
    return result


@timer
@print_result
def part1():
    return ",".join(map(str, run(A)))


@timer
@print_result
def part2():
    og_program = P.copy()

    a = 51878397
    a = 52805575875069
    prev = 0
    while True:
        x = run(a)
        if x[:10] == [2, 4, 1, 3, 7, 5, 4, 0, 1, 3]:
            print(a, len(x), a - prev, x)
            prev = a
        if x == og_program:
            return a
        # if len(x) < 16:
        #     print(a)
        #     a *= 2
        a += 2097152 * 1024


def main(args=None):
    part1()
    part2()


if __name__ == "__main__":
    main(argv[1:])
