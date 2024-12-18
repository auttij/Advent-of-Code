from re import findall
from aocHelpers.decorators import timer_print


def solve_rec(line, possible_operators):
    target, *rest = line
    l = len(rest)

    ops = {
        "p": lambda x, y: x + y,
        "m": lambda x, y: x * y,
        "c": lambda x, y: int(f"{x}{y}"),
    }

    def dfs(index, current_value):
        if index == l:
            return current_value == target

        for operator in possible_operators:
            next_value = ops[operator](current_value, rest[index])
            if next_value > target:
                continue
            if dfs(index + 1, next_value):
                return True
        return False

    return target if dfs(1, rest[0]) else 0


@timer_print
def main(lines):
    part1 = 0
    part2 = 0
    for line in lines:
        result1 = solve_rec(line, "mp")
        part1 += result1
        if not result1:
            part2 += solve_rec(line, "cpm")

    print(f"{part1 = }")
    print(f"part2 = {part2 + part1}")


if __name__ == "__main__":

    lines = [tuple(map(int, findall(r"\d+", line))) for line in open("input2.txt")]
    main(lines)
