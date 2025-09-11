from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import defaultdict
from operator import itemgetter


def parse_instruction(line):
    parts = line.split()
    return {
        "register": parts[0],
        "operation": parts[1],
        "value": int(parts[2]),
        "condition": {
            "register": parts[4],
            "operator": parts[5],
            "value": int(parts[6]),
        },
    }


def update_registers(registers, instruction):
    if instruction["operation"] == "inc":
        registers[instruction["register"]] += instruction["value"]
    else:
        registers[instruction["register"]] -= instruction["value"]


def process_condition(registers, condition):
    creg, operator, cval = itemgetter("register", "operator", "value")(condition)
    return eval(f"{registers[creg]} {operator} {cval}")


def process_instructions(arr):
    registers = defaultdict(int)
    max_value_ever = float("-inf")

    for line in arr:
        instruction = parse_instruction(line)
        if process_condition(registers, instruction["condition"]):
            update_registers(registers, instruction)
            current_max = max(registers.values())
            if current_max > max_value_ever:
                max_value_ever = current_max

    return max(registers.values()), max_value_ever


@timer
@print_result
def part1(arr):
    max_val, _ = process_instructions(arr)
    return max_val


@timer
@print_result
def part2(arr):
    _, max_val_ever = process_instructions(arr)
    return max_val_ever


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
