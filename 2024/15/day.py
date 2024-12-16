from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def parse(arr):
    maze = []
    out = []
    i = 0
    half = False
    while i < len(arr):
        if len(arr[i]) == 0:
            half = True
        elif not half:
            maze.append(list(arr[i]))
        else:
            out.append(arr[i])
        i += 1
    return maze, list("".join(out))


def pp(maze):
    for y, row in enumerate(maze):
        print("".join(row))


@timer
@print_result
def part1(maze, inst):

    h = len(maze)
    w = len(maze[0])

    for y, row in enumerate(maze):
        for x, val in enumerate(row):
            if val == "@":
                start = (y, x)

    def can_move(direction, start):
        dy, dx = direction
        sy, sx = start
        ny, nx = sy + dy, sx + dx
        boxes = False
        while 0 <= nx < w and 0 <= ny < h:
            if maze[ny][nx] == "#":
                return boxes, None
            elif maze[ny][nx] == "O":
                boxes = True
            elif maze[ny][nx] == ".":
                return boxes, (ny, nx)
            ny, nx = ny + dy, nx + dx
        return boxes, None

    y, x = start
    dirs = {"<": (0, -1), "^": (-1, 0), "v": (1, 0), ">": (0, 1)}
    for ins in inst:
        dire = dirs[ins]

        boxes, new_pos = can_move(dire, (y, x))
        if new_pos == None:
            continue

        # print(ins, boxes, (y, x), new_pos)

        dy, dx = dire
        ny, nx = y + dy, x + dx
        if boxes:
            # move box

            ney, nex = new_pos
            maze[ney][nex] = maze[ny][nx]
        maze[ny][nx] = "@"
        maze[y][x] = "."
        y, x = ny, nx

        # pp(maze)

    # pp(maze)

    s = 0
    for y, row in enumerate(maze):
        for x, val in enumerate(row):
            if val == "O":
                s += 100 * y + x
    return s


@timer
@print_result
def part2(maze, instructions):

    h = len(maze)
    w = len(maze[0])
    new_maze = []
    for y, row in enumerate(maze):
        new_row = []
        for x, val in enumerate(row):
            if val == "#":
                new_row.append("#")
                new_row.append("#")
            if val == "O":
                new_row.append("[")
                new_row.append("]")
            if val == ".":
                new_row.append(".")
                new_row.append(".")
            if val == "@":
                new_row.append("@")
                new_row.append(".")
        new_maze.append(new_row)

    for y, row in enumerate(new_maze):
        for x, val in enumerate(row):
            if val == "@":
                start = (y, x)

    dirs = {"<": (0, -1), "^": (-1, 0), "v": (1, 0), ">": (0, 1)}

    def can_move(ins, start):
        direction = dirs[ins]
        dy, dx = direction

        def find_rec(pos, depth):
            py, px = pos
            npy, npx = py + dy, px + dx
            if new_maze[npy][npx] == ".":
                return [(True, (depth, (py, px), (npy, npx)))]
            elif new_maze[npy][npx] == "#":
                return [(False, (depth, None, None))]
            elif new_maze[npy][npx] == "[":
                if ins in "^v":
                    return (
                        [(True, (depth, (py, px), (npy, npx)))]
                        + find_rec((npy, npx), depth + 1)
                        + find_rec((npy, npx + 1), depth + 1)
                    )
                else:
                    return (
                        [(True, (depth, (py, px), (npy, npx)))]
                        + find_rec((npy, npx + 1), depth + 2)
                        + [(True, (depth + 1, (npy, npx), (npy, npx + 1)))]
                    )
            elif new_maze[npy][npx] == "]":
                if ins in "^v":
                    return (
                        [(True, (depth, (py, px), (npy, npx)))]
                        + find_rec((npy, npx), depth + 1)
                        + find_rec((npy, npx - 1), depth + 1)
                    )
                else:
                    return (
                        [(True, (depth, (py, px), (npy, npx)))]
                        + find_rec((npy, npx - 1), depth + 2)
                        + [(True, (depth + 1, (npy, npx), (npy, npx - 1)))]
                    )

        possible, moves = zip(*find_rec(start, 0))
        return all(possible), moves

    y, x = start
    dirs = {"<": (0, -1), "^": (-1, 0), "v": (1, 0), ">": (0, 1)}
    for ins in instructions:
        dire = dirs[ins]
        possible, moves = can_move(ins, (y, x))
        if not possible:
            continue
        dy, dx = dire
        ny, nx = y + dy, x + dx

        sor = sorted(moves, key=lambda x: x[0])
        sor_moves = [move for i, move in enumerate(sor) if move not in sor[i + 1 :]][
            ::-1
        ]

        for diff in sor_moves:
            depth, move_from, move_to = diff
            py, px = move_from
            my, mx = move_to

            new_maze[my][mx] = new_maze[py][px]
            new_maze[py][px] = "."
            if depth == 0:
                y, x = my, mx
    s = 0
    for y, row in enumerate(new_maze):
        for x, val in enumerate(row):
            if val == "[":
                s += 100 * y + x
    return s


def main(args=None):
    unp = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    maze, inst = parse(unp)
    part1(maze.copy(), inst)
    part2(maze.copy(), inst)


if __name__ == "__main__":
    main(argv[1:])
