import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import rotate
from itertools import permutations


def scramble(password, instructions):
    for line in instructions:
        splt = line.split(" ")
        if splt[0] == "swap":
            if splt[1] == "position":
                p1, p2 = int(splt[2]), int(splt[-1])
                password[p1], password[p2] = password[p2], password[p1]
            elif splt[1] == "letter":
                p = "".join(password)
                l1, l2 = splt[2], splt[-1]
                p = p.replace(l1, ".")
                p = p.replace(l2, l1)
                p = p.replace(".", l2)
                password = list(p)
        elif splt[0] == "reverse":
            p1, p2 = int(splt[2]), int(splt[-1]) + 1
            password = password[:p1] + password[p1:p2][::-1] + password[p2:]
        elif splt[0] == "rotate":
            if splt[1] == "based":
                letter = splt[-1]
                ind = password.index(letter)
                rot = 1 + ind
                if ind >= 4:
                    rot += 1
                password = rotate(password, -rot)
            else:
                step = int(splt[2])
                if splt[1] == "right":
                    step = -step
                password = rotate(password, step)
        elif splt[0] == "move":
            p1, p2 = int(splt[2]), int(splt[-1])
            v1 = password.pop(p1)
            password.insert(p2, v1)
    return password


@timer
@print_result
def exercise1(arr):
    password = list("abcdefgh")
    return "".join(scramble(password, arr))


@timer
@print_result
def exercise2(arr):
    target = "fbgdceah"
    for i in permutations(target, len(target)):
        pw = "".join(scramble(list(i), arr))
        if pw == target:
            return "".join(i)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
