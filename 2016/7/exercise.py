import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def abba(s):
    return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]


def has_abba(s):
    for i in range(len(s) - 3):
        if abba(s[i : i + 4]):
            return True
    return False


@timer
@print_result
def exercise1(arr):
    TLS = 0
    for line in arr:
        parts = line.split("[")
        normal = [parts[0]]
        brackets = []
        for part in parts[1:]:
            p1, p2 = part.split("]")
            brackets.append(p1)
            normal.append(p2)
        if any(map(has_abba, normal)) and not any(map(has_abba, brackets)):
            TLS += 1
    return TLS


def aba(s):
    return s[0] == s[2] and s[0] != s[1]


def get_abas(s):
    out = []
    for i in range(len(s) - 2):
        if aba(s[i : i + 3]):
            out.append(s[i : i + 3])
    return out


def to_bab(s):
    return s[1] + s[0] + s[1]


@timer
@print_result
def exercise2(arr):
    SLI = 0

    for line in arr:
        parts = line.split("[")
        normal = [parts[0]]
        brackets = []
        for part in parts[1:]:
            p1, p2 = part.split("]")
            brackets.append(p1)
            normal.append(p2)

        aba_lists = list(map(get_abas, normal))
        abas = list(set([x for y in aba_lists for x in y]))
        babs = list(map(to_bab, abas))
        found = False
        for bracket in brackets:
            for bab in babs:
                if bab in bracket:
                    found = True
        if found:
            SLI += 1
    return SLI


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
