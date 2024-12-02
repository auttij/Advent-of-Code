import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def process(mem, arr):

    lim = len(arr)
    i = 0
    while 0 <= i < lim:
        instruction = arr[i]
        cmd = instruction[:3]
        reg = instruction[4]

        if cmd == "hlf":
            mem[reg] = mem[reg] // 2
        elif cmd == "tpl":
            mem[reg] = mem[reg] * 3
        elif cmd == "inc":
            mem[reg] += 1
        elif cmd == "jmp":
            val = None
            if "+" in instruction:
                val = int(instruction.split("+")[1])
            elif "-" in instruction:
                val = -int(instruction.split("-")[1])
            i += val
            continue
        elif cmd == "jie":
            val = int(instruction.split("+")[1])
            if mem[reg] % 2 == 0:
                i += val
                continue
        elif cmd == "jio":
            val = int(instruction.split("+")[1])
            if mem[reg] == 1:
                i += val
                continue
        i += 1
    return mem["b"]


@timer
@print_result
def exercise1(arr):
    mem = {
        "a": 0,
        "b": 0,
    }
    return process(mem, arr)


@timer
@print_result
def exercise2(arr):
    mem = {
        "a": 1,
        "b": 0,
    }
    return process(mem, arr)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
