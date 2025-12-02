from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init
import re


def get_info(log):
    p = r"\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]\s*(.*)"
    result = re.search(p, log)
    return result.groups()


@aoc_part
def part1(arr):

    sleep_log = {}

    guard = None
    sleeping = None
    for log in sorted(arr):
        year, month, date, hour, minute, text = get_info(log)
        p = r"Guard #(\d+)"
        match = re.search(p, text)
        if match:
            guard = match.groups()[0]
            if guard not in sleep_log:
                sleep_log[guard] = []

        if text == "falls asleep":
            sleeping = int(minute)
        if text == "wakes up":
            sleep_log[guard].append((sleeping, int(minute)))
            sleeping = None

    sleepiest = None
    sleeps = 0
    for k, v in sleep_log.items():
        total = 0
        for a, b in v:
            total += b - a
        if total > sleeps:
            sleeps = total
            sleepiest = k

    sleepiest_minute = [0] * 60
    for a, b in sleep_log[sleepiest]:
        for i in range(a, b):
            sleepiest_minute[i] += 1
    res = max(sleepiest_minute)
    ind = sleepiest_minute.index(res)
    return int(sleepiest) * ind


@aoc_part
def part2(arr):

    sleep_log = {}

    guard = None
    sleeping = None
    for log in sorted(arr):
        year, month, date, hour, minute, text = get_info(log)
        p = r"Guard #(\d+)"
        match = re.search(p, text)
        if match:
            guard = match.groups()[0]
            if guard not in sleep_log:
                sleep_log[guard] = []

        if text == "falls asleep":
            sleeping = int(minute)
        if text == "wakes up":
            sleep_log[guard].append((sleeping, int(minute)))
            sleeping = None

    sleepiest = None
    sleeps = 0
    minute = 0

    for k, v in sleep_log.items():
        sleepiest_minute = [0] * 60
        for a, b in v:
            for i in range(a, b):
                sleepiest_minute[i] += 1

        res = max(sleepiest_minute)
        ind = sleepiest_minute.index(res)

        if res > sleeps:
            sleeps = res
            minute = ind
            sleepiest = k

    return int(sleepiest) * minute


def parse_input(raw):
    return raw.splitlines()


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
