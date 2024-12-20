from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import deque


def bfs(grid):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "S":
                start = (y, x)
            if val == "E":
                end = (y, x)

    q = deque()
    q.append((start, 0))
    seen = set()
    while q:
        pos, dist = q.popleft()
        if pos in seen:
            continue
        distances[pos] = dist
        if pos == end:
            return dist
        seen.add(pos)
        y, x = pos
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if 0 <= y + dy < h and 0 <= x + dx < w and grid[y + dy][x + dx] != "#":
                q.append(((y + dy, x + dx), dist + 1))


def get_reachable(y, x, max_dist):
    reachable = []
    for dy in range(-max_dist, max_dist + 1):
        remaining_dist = max_dist - abs(dy)
        for dx in range(-remaining_dist, remaining_dist + 1):
            if dy == dx == 0:
                continue
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] != "#":
                reachable.append((ny, nx))
    return reachable


def solve(cheat_dist):
    res = 0
    for pos in distances.keys():
        y, x = pos
        reachable = get_reachable(y, x, cheat_dist)
        for dy, dx in reachable:
            cost = abs(x - dx) + abs(y - dy)
            savings = distances[(y, x)] - (distances[(dy, dx)] + cost)
            if savings >= 100:
                res += 1
    return res


@timer
@print_result
def part1():
    return solve(2)


@timer
@print_result
def part2():
    return solve(20)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    global grid, w, h, distances
    grid = arr
    h = len(arr)
    w = len(arr[0])
    distances = {}
    bfs(grid)

    part1()
    part2()


if __name__ == "__main__":
    main(argv[1:])
