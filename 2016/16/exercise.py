import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def reverse(n, no_of_bits):
    result = 0
    for i in range(no_of_bits):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result


# def dragon_curve(a):
#     l = len(str(a))
#     print(f"{a = }", l)
#     reversed = reverse(a, l)
#     inverse = reversed ^ (2 ** (l)) - 1
#     b = bin(inverse)[2:]

#     print(reversed, inverse)
#     print(bin(reversed)[2:], bin(inverse)[2:], b)

#     result = f"{a}0{b}"
#     print(result)
#     print()

#     return result


def dragon_curve(a):
    rev = a[::-1]
    temp = rev.replace("1", "2")
    temp2 = temp.replace("0", "1")
    b = temp2.replace("2", "0")
    return f"{a}0{b}"


def checksum(data):
    output = []
    for i in range(0, len(data), 2):
        if data[i] == data[i + 1]:
            output.append("1")
        else:
            output.append("0")
    output = "".join(output)
    if len(output) % 2 == 0:
        return checksum(output)
    else:
        return output


def calculate_checksum(arr, length):
    data = arr
    while len(data) < length:
        data = dragon_curve(data)
    cut = data[:length]
    cs = checksum(cut)
    return cs


@timer
@print_result
def exercise1(arr, length):
    return calculate_checksum(arr, length)


@timer
@print_result
def exercise2(arr, length):
    return calculate_checksum(arr, length)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr[0], 272)
    exercise2(arr[0], 35651584)


if __name__ == "__main__":
    main(argv[1:])
