import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from hashlib import md5


@timer
@print_result
def exercise1(arr):
    base = arr[0]
    pwd = []

    i = 0
    while len(pwd) < 8:
        m = md5()
        m.update(bytes(base + str(i), "utf8"))
        if m.hexdigest()[:5] == "00000":
            pwd.append(m.hexdigest()[5])
        i += 1
    return "".join(pwd)


@timer
@print_result
def exercise2(arr):
    base = arr[0]
    pwd = ["" for i in range(8)]
    hits = 0

    i = 0
    while hits < 8:
        m = md5()
        m.update(bytes(base + str(i), "utf8"))
        hd = m.hexdigest()
        if hd[:5] == "00000" and hd[5].isdigit():
            pos = int(hd[5])
            if int(hd[5]) < 8 and pwd[pos] == "":
                pwd[pos] = hd[6]
                hits += 1
        i += 1
    return "".join(pwd)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
