import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import deque
from itertools import combinations, product


def create_state(arr):
    floors = [(), (), (), ()]
    for i, line in enumerate(arr[:-1]):
        things = line.split("contains a ")[1].split(" a ")
        for thing in things:
            name = thing[:2].upper() + thing.split(" ")[1][0].upper()
            floors[i] = floors[i] + (name,)
    return floors


def pretty_print(elevator, floors):
    flat = sorted([x for y in floors for x in y])
    for i in range(4)[::-1]:
        floor = floors[i]
        row = [f"F{i+1}"]
        if elevator == i:
            row.append("E")
        else:
            row.append(".")

        for thing in flat:
            if thing in floor:
                row.append(thing)
            else:
                row.append(".  ")
        print(" ".join(row))
    print()


def is_ok(floors):
    for floor in floors:
        generators = [i for i in floor if i[-1] == "G"]
        microchips = [i for i in floor if i[-1] == "M"]
        for m in microchips:
            if len(generators) > 0 and f"{m[:2]}G" not in generators:
                return False
    return True


def is_finished(floors):
    return len(floors[0]) == len(floors[1]) == len(floors[2]) == 0


def next_floors(floor):
    for i in (-1, 1):
        new_floor = floor + i
        if 0 <= new_floor <= 3:
            yield new_floor


def make_move(state, move, old_floor):
    new_state = state.copy()
    new_floor, items = move
    new_state[old_floor] = tuple(filter(lambda x: x not in items, new_state[old_floor]))
    new_state[new_floor] = new_state[new_floor] + items
    return new_state


def filter_moves(elevator, floors, move):
    next_elevator, moved_items = move
    if not is_ok([moved_items]):
        return False
    if elevator > next_elevator:
        if sum([len(floors[i]) for i in range(elevator)]) == 0:
            return False
    return True


def fingerprint(elevator, floors):
    out = [str(elevator)]
    lookup = {}
    seen = 0
    for i, floor in enumerate(floors):
        for item in floor:
            if item[:2] not in lookup:
                lookup[item[:2]] = f"{seen}"
                seen += 1
            out.append(f"{lookup[item[:2]]}{item[-1]}{i}")
    return "".join(out)


def solve(floors):
    elevator = 0

    seen = set()

    # elevator, state, [previous floor, moved things], nof_steps
    checks = 0
    q = deque()
    q.append((0, floors, (-1, ()), 0, []))
    max_depth = 0

    while q:
        elevator, floors, prev, depth, path = q.popleft()
        fp = fingerprint(elevator, floors)
        if fp not in seen:
            seen.add(fp)
        else:
            continue
        checks += 1
        if depth > max_depth:
            max_depth = depth
            print(max_depth)

        if is_finished(floors):
            print(checks)
            return depth, path
        floor = floors[elevator]
        item_sets = [(item,) for item in floor] + list(combinations(floor, 2))
        moves = list(product(list(next_floors(elevator)), item_sets))
        moves = filter(lambda x: filter_moves(elevator, floors, x), moves)
        possible_moves = []

        for move in moves:
            if move == prev:
                continue
            new_elevator, moved_items = move
            new_floors = make_move(floors, move, elevator)
            if not is_ok(new_floors):
                continue
            nfp = fingerprint(new_elevator, new_floors)
            if nfp in seen:
                continue

            possible_moves.append(
                (new_elevator, new_floors, (elevator, moved_items), depth + 1)
            )

        up = [move for move in possible_moves if move[0] > elevator]
        up_high = max(map(lambda x: len(x[2][1]), up)) if up else 0
        down = [move for move in possible_moves if move[0] < elevator]
        down_low = min(map(lambda x: len(x[2][1]), down)) if down else 0

        for move in possible_moves:
            new_elevator, new_floors, old_move, new_depth = move
            elevator, moved_items = old_move
            if up_high == 2 and new_elevator > elevator and len(moved_items) == 1:
                continue
            if down_low == 1 and new_elevator < elevator and len(moved_items) == 2:
                continue
            q.append(
                (
                    new_elevator,
                    new_floors,
                    (elevator, moved_items),
                    new_depth,
                    path + [(new_elevator, new_floors)],
                )
            )


@timer
@print_result
def exercise1(floors):
    depth, path = solve(floors)

    print("\n0")
    pretty_print(0, floors)
    for i, step in enumerate(path, start=1):
        print(i)
        pretty_print(*step)

    print("part 2:" depth + 24)
    return depth


@timer
@print_result
def exercise2(floors):
    floors[0] = floors[0] + ("ELG", "ELM", "DIG", "DIM")
    print(floors)
    depth, path = solve(floors)

    print("\n0")
    pretty_print(0, floors)
    for i, step in enumerate(path, start=1):
        print(i)
        pretty_print(*step)

    return depth


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    state = create_state(arr)
    exercise1(state.copy())
    # exercise2(state.copy())


if __name__ == "__main__":
    main(argv[1:])
