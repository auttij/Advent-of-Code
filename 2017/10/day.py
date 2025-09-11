from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def knot_hash(data, arr, pos=0, skip_size=0):
    for length in arr:
        # Reverse the order of the elements in the list
        sublist = (
            data[pos : pos + length] + data[0 : max(0, (pos + length) - len(data))]
        )
        sublist.reverse()
        for i in range(length):
            data[(pos + i) % len(data)] = sublist[i]

        pos = (pos + length + skip_size) % len(data)
        skip_size += 1
    return data, pos, skip_size


@timer
@print_result
def part1(arr):
    inputs = [int(x) for x in arr.split(",")]
    data = list(range(0, 256))
    data, _, _ = knot_hash(data, inputs)
    return data[0] * data[1]


@timer
@print_result
def part2(arr):
    extra = [17, 31, 73, 47, 23]
    inputs = [ord(x) for x in arr.strip()] + extra
    pos = 0
    skip_size = 0
    data = list(range(0, 256))

    for _ in range(64):
        data, pos, skip_size = knot_hash(data, inputs, pos, skip_size)

    out = []
    for i in range(16):
        block = data[i * 16 : (i + 1) * 16]
        block_hash = block[0]
        for num in block[1:]:
            block_hash ^= num
        out.append(hex(block_hash)[2:])
    return "".join(f"{x}" for x in out)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy()[0])
    part2(arr.copy()[0])


if __name__ == "__main__":
    main(argv[1:])
