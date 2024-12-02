import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def unot(value):
    value &= 0xFFFF
    completement = ~value
    return completement & 0xFFFF


@timer
@print_result
def exercise1(arr):

    stack = arr
    signals = {}
    while len(stack) > 0:
        top = stack.pop(0)
        instruction, target = top
        print(top)

        result = None
        if instruction.isdigit():
            result = int(instruction)
        else:
            splt = instruction.split(" ")
            if len(splt) == 2:
                if splt[1] not in signals:
                    stack.append(top)
                    continue
                result = unot(signals[splt[1]])
            elif len(splt) == 1:
                if splt[0] not in signals:
                    stack.append(top)
                    continue
                result = signals[splt[0]]
            else:
                if (not splt[0].isdigit() and splt[0] not in signals) or (
                    not splt[2].isdigit() and splt[2] not in signals
                ):
                    stack.append(top)
                    continue
                if splt[1] == "AND":
                    a = None
                    if splt[0].isdigit():
                        a = int(splt[0])
                    else:
                        a = signals[splt[0]]
                    result = a & signals[splt[2]]
                elif splt[1] == "OR":
                    result = signals[splt[0]] | signals[splt[2]]
                elif splt[1] == "LSHIFT":
                    result = signals[splt[0]] << int(splt[2])
                elif splt[1] == "RSHIFT":
                    result = signals[splt[0]] >> int(splt[2])
        signals[target] = result
    return signals["a"]


@timer
@print_result
def exercise2(arr):
    ## Manually change part 1 result to b
    pass


def main(args=None):
    input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    arr = [tuple(i.split(" -> ")) for i in input]
    exercise1(arr[::])
    exercise2(arr[::])


if __name__ == "__main__":
    main(argv[1:])
