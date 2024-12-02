import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def solve(arr, part2=False):
    bots = {}
    instructions = {}
    outputs = {}

    for line in arr:
        if line[:5] == "value":
            splt = line.split(" ")
            val = int(splt[1])
            bot = int(splt[-1])
            if bot not in bots:
                bots[bot] = []
            bots[bot].append(val)
        else:
            splt = line.split(" ")
            bot = int(splt[1])
            low = splt[5]
            low_idx = int(splt[6])

            high = splt[-2]
            high_idx = int(splt[-1])

            instructions[bot] = [[low, low_idx], [high, high_idx]]

    current = [k for k, v in bots.items() if len(v) == 2][0]
    stack = [current]

    while len(stack) > 0:
        bot = stack.pop(0)
        low_ins, high_ins = instructions[bot]
        low = min(bots[bot])
        high = max(bots[bot])

        if not part2 and low == 17 and high == 61:
            return bot

        low_idx = low_ins[1]
        if low_ins[0] == "output":
            outputs[low_idx] = low
        elif low_ins[0] == "bot":
            if low_idx not in bots:
                bots[low_idx] = []
            bots[low_idx].append(low)
            if len(bots[low_idx]) == 2:
                stack.append(low_idx)

        high_idx = high_ins[1]
        if high_ins[0] == "output":
            outputs[high_idx] = high
        elif high_ins[0] == "bot":
            if high_idx not in bots:
                bots[high_idx] = []
            bots[high_idx].append(high)
            if len(bots[high_idx]) == 2:
                stack.append(high_idx)
    return outputs[0] * outputs[1] * outputs[2]


@timer
@print_result
def exercise1(arr):
    return solve(arr)


@timer
@print_result
def exercise2(arr):
    return solve(arr, True)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
