from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init


def get_orientations(present):
    result = []
    seen = set()

    def rotate(shape):
        return ["".join(row) for row in zip(*shape[::-1])]

    def flip(shape):
        return [row[::-1] for row in shape]

    def norm(s):
        return "\n".join(s)

    current = present
    for _ in range(4):  # 4 rotations
        # rotation
        n = norm(current)
        if n not in seen:
            seen.add(n)
            result.append(current)

        # flipped rotation
        flipped = flip(current)
        nf = norm(flipped)
        if nf not in seen:
            seen.add(nf)
            result.append(flipped)

        current = rotate(current)

    return result


def find_first_empty(board):
    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if not val:
                return (y, x)
    return None

def find_next_empty(board, prev):
    r, c = prev
    seen = False
    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if y == r and x == c:
                seen = True
            elif seen and not val:
                return (y, x)
    return None



def str_board(board):
    out = []
    for row in board:
        row_str = []
        for val in row:
            if val:
                row_str.append("#")
            else:
                row_str.append(".")
        out.append(row_str)
    return out


def print_board(board, highlight=None):
    str_repr = str_board(board)
    if highlight:
        str_repr[highlight[0]][highlight[1]] = "A"
    print("\n".join(["".join(row) for row in str_repr]))
    print()


def try_place(board, shape, r, c):
    rows, cols = len(board), len(board[0])
    for y, row in enumerate(shape):
        for x, val in enumerate(row):
            if rows <= r + y or cols <= c + x:
                return False
            if val == "#" and board[r + y][c + x]:
                return False
    return True


def place(board, shape, r, c, val):
    for y, row in enumerate(shape):
        for x, char in enumerate(row):
            if char == "#":
                board[r + y][c + x] = val
    return board


def fit_presents(board, counts, presents):
    if all([i == 0 for i in counts]):
        return True
    pos = find_first_empty(board)
    if pos is None:
        return False

    while pos is not None:
        r, c = pos

        for present_idx in range(len(presents)):
            if counts[present_idx] == 0:
                continue

            for orientation in presents[present_idx]:
                if try_place(board, orientation, r, c):
                    place(board, orientation, r, c, True)
                    counts[present_idx] -= 1

                    # print_board(board)
                    if fit_presents(board, counts, presents):
                        return True

                    place(board, orientation, r, c, False)
                    counts[present_idx] += 1
        pos = find_next_empty(board, (r, c))
    return False


@aoc_part
def part1(data):
    presents, shapes = data
    count = ["".join(i).count("#") for i in presents]
    presents = [get_orientations(p) for p in presents]

    total = 0
    for i, s in enumerate(shapes):
        size = s[0] * s[1]
        t = sum([count[i] * v for i, v in enumerate(s[2:])])
        if t > size:
            continue
        total += 1

    #     width, height = s[0], s[1]
    #     board = [[False] * width for _ in range(height)]
    #     if fit_presents(board, list(s[2:]), presents):
    #         print(i, "True")
    #         total += 1
    return total


@aoc_part
def part2(data):
    pass


def parse_input(raw):
    import re

    data = raw.split("\n\n")
    presents = [i.split()[1:4] for i in data[:6]]
    shapes = [
        tuple(map(int, re.findall(r"-?\d+", line))) for line in data[6].split("\n")
    ]
    return (presents, shapes)


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
