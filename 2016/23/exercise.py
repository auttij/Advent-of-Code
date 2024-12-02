import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


IDXS = ["a", "b", "c", "d"]


def get_val(vals, x):
    if x:
        if x.isalpha():
            return vals[x]
        else:
            return int(x)
    else:
        return None


def skip(cmd, xi, yi):
    if (cmd == "cpy" and xi.isdigit() and yi.isdigit()) or (
        cmd in ["inc", "dec"] and xi.isdigit()
    ):
        return True
    return False


def process(vals, arr):
    instructions = arr
    ins = 0
    cmd_idx = 0
    max_idx = 0
    while cmd_idx < len(instructions):
        ins += 1
        splt = instructions[cmd_idx]
        if len(splt) == 2:
            splt.append(None)
        cmd, xi, yi = splt

        # print(ins, cmd_idx)
        # print(vals, splt, cmd)

        if skip(*splt):
            # print("skip")
            cmd_idx += 1
            continue

        x = get_val(vals, xi)
        y = get_val(vals, yi)

        if cmd == "cpy":
            # print("cpy")
            vals[yi] = x
        if cmd == "inc":
            # print("inc")
            vals[xi] += 1
        if cmd == "dec":
            # print("dec")
            vals[xi] -= 1
        if cmd == "tgl":
            # print("tgl")
            if cmd_idx + x < len(instructions):
                target = instructions[cmd_idx + x]
                target_cmd = target[0]
                if target_cmd in ["inc", "dec", "tgl"]:
                    target[0] = "inc"
                if target_cmd in ["jnz", "cpy"]:
                    target[0] = "jnz"
                instructions[cmd_idx + x] = target

        if cmd == "jnz" and x != 0:
            # print("jnz")
            if cmd_idx >= 2:
                prev1 = instructions[cmd_idx - 1]
                prev2 = instructions[cmd_idx - 2]

                c1 = prev1[0]
                c2 = prev2[0]
                xi1 = prev1[1]
                x1 = get_val(vals, prev1[1])
                xi2 = prev2[1]
                x2 = get_val(vals, prev2[1])

                if y == -2 and c2 == "inc" and c1 == "dec":
                    vals[xi2] += x1
                    vals[xi1] = 0
                    cmd_idx += 1
                    continue
                elif y == -2 and c2 == "dec" and c1 == "inc":
                    vals[xi1] += x2
                    vals[xi2] = 0
                    cmd_idx += 1
                    continue
                elif y == -2 and c2 == "inc" and c1 == "inc" and x1 < 0:
                    vals[xi2] -= x1
                    vals[xi1] = 0
                    cmd_idx += 1
                    continue
                elif y == -2 and c2 == "inc" and c1 == "inc" and x2 < 0:
                    vals[xi1] -= x2
                    vals[xi2] = 0
                    cmd_idx += 1
                    continue
                elif y == -5:
                    xi4 = instructions[cmd_idx - 4][1]
                    prev5 = instructions[cmd_idx - 5]
                    x5 = get_val(vals, prev5[1])
                    prev3 = instructions[cmd_idx - 3]
                    xi3 = prev3[1]
                    x3 = get_val(vals, xi3)
                    vals[xi4] += x5 * x1
                    vals[xi3] = 0
                    vals[xi1] = 0
                    cmd_idx += 1
                    continue

            cmd_idx += y
        else:
            cmd_idx += 1
        if cmd_idx == 18:
            max_idx = cmd_idx
            print(cmd_idx)
            print(vals)
            print(instructions[: cmd_idx + 1])
        # print(instructions)
        # print()
    return vals


@timer
@print_result
def exercise1(arr):
    lines = [line.split(" ") for line in arr]
    vals = {"a": 7, "b": 0, "c": 0, "d": 0}
    # for line in lines:
    #     print(line)

    return process(vals, lines)["a"]


@timer
@print_result
def exercise2(arr):
    pass


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
