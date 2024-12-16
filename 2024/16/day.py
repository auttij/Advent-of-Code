from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import deque


def find_start_end(arr):
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            if val == "E":
                end = (y, x)
            if val == "S":
                start = (y, x)
    return start, end


def neighbors(key):
    if key == "E":
        return "SEN"
    if key == "S":
        return "ESW"
    if key == "W":
        return "SWN"
    if key == "N":
        return "ENW"


def cmp(nex, cur):
    return nex != "#"


def bfs(grid, start, end, cmp, part2=False):
    dirs = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}
    q = deque()
    q.append((start, 0, "E", [start]))
    seen = {}
    lowest = float("inf")
    tiles = {}

    while q:
        pos, dist, dir, path = q.popleft()

        if pos == end:
            if dist <= lowest:
                lowest = dist
                if part2:
                    if lowest not in tiles:
                        tiles[lowest] = set()
                    tiles[lowest].update(path)

        if (pos, dir) in seen:
            if not part2 or (part2 and seen[(pos, dir)] < dist):
                continue
        seen[(pos, dir)] = dist

        x, y = pos
        for next_dir in neighbors(dir):
            dx, dy = dirs[next_dir]
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and cmp(grid[x + dx][y + dy], grid[x][y])
            ):
                if next_dir == dir:
                    q.append(
                        (
                            (x + dx, y + dy),
                            dist + 1,
                            next_dir,
                            path + [(x + dx, y + dy)],
                        )
                    )
                else:
                    q.append(((x, y), dist + 1000, next_dir, path))

    if part2:
        return tiles[lowest]
    else:
        return lowest


@timer
@print_result
def part1(arr):
    start, end = find_start_end(arr)
    return bfs(arr, start, end, cmp)


@timer
@print_result
def part2(arr):
    start, end = find_start_end(arr)
    return len(bfs(arr, start, end, cmp, part2=True))


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
