import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def reindeer_distance(speed, last, rest, time):
    cycle = last + rest
    full = time // cycle
    remainder = time - full * cycle
    if remainder > last:
        remainder = last
    return (full * last + remainder) * speed


@timer
@print_result
def exercise1(arr):
    time = 2503
    return max([reindeer_distance(*reindeer, time) for reindeer in arr])


def second(prev, time, speed, last, rest):
    moving = (time % (last + rest)) < last
    # print(time, last + rest, time % (last + rest))
    if moving:
        return prev + speed
    else:
        return prev


@timer
@print_result
def exercise2(arr):
    points = [0 for i in range(len(arr))]
    dist = [0 for i in range(len(arr))]
    for time in range(2503):
        for i, reindeer in enumerate(arr):
            dist[i] = second(dist[i], time, *reindeer)

        max_val = max(dist)
        for i, val in enumerate(dist):
            if val == max_val:
                points[i] += 1
    return max(points)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
