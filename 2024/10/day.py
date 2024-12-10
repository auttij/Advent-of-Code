from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import bfs


def dfs(grid, start, end, cmp):
    stack = []
    stack.push(start)
    seen = set()
    while stack:
        pos = stack.pop(-1)
        if pos == end:
            return stack
        if pos in seen:
            continue
        seen.add(pos)
        y, x = pos
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and cmp(grid[y + dy][x + dx], grid[y][x])
            ):
                stack.append((y + dy, x + dx))


@timer
@print_result
def part1(arr):
    zeroes = []
    nines = []
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            if val == "0":
                zeroes.append((y, x))
            if val == "9":
                nines.append((y, x))

    def cmp(nex, cur):
        if not (nex.isdigit() and cur.isdigit()):
            return False
        if int(nex) - int(cur) == 1:
            # print(nex, cur)
            return True
        return False

    can_reach = 0
    for start in zeroes:
        score = 0
        for nine_pos in nines:
            if bfs(arr, start, nine_pos, cmp) < 200:
                # print(start, nine_pos)
                score += 1
        # print(start, score)
        can_reach += score
    return can_reach
    pass


from collections import deque


def bfs2(grid, start, end, cmp):
    out = 0
    q = deque()
    q.append((start, 0))
    while q:
        pos, dist = q.popleft()
        if dist > 9:
            continue
        if dist == 9:
            out += 1
        x, y = pos
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and cmp(grid[x + dx][y + dy], grid[x][y])
            ):
                q.append(((x + dx, y + dy), dist + 1))
    return out


@timer
@print_result
def part2(arr):
    zeroes = []
    nines = []
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            if val == "0":
                zeroes.append((y, x))
            if val == "9":
                nines.append((y, x))

    def cmp(nex, cur):
        if not (nex.isdigit() and cur.isdigit()):
            return False
        if int(nex) - int(cur) == 1:
            # print(nex, cur)
            return True
        return False

    can_reach = 0
    for start in zeroes:
        score = bfs2(arr, start, (0, 0), cmp)
        # print(start, score)
        can_reach += score
    return can_reach
    pass


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
