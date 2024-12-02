import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def manhattan(x1, x2, y1, y2):
	return abs(x1 - x2) + abs(y1 - y2)

@timer
@print_result
def exercise1(arr):
	TARGET_Y = 2000000

	beacons = set((bx, by) for sx, sy, bx, by in arr)
	no_beacons = set()

	for (sx, sy, bx, by) in arr[3:4]:
		min_manhattan = abs(sx-bx) + abs(sy-by)

		for dx in (1, -1):
			dist = abs(sy - TARGET_Y)
			x = sx
			while dist <= min_manhattan:
				no_beacons.add((x, TARGET_Y))
				x += dx
				dist += 1
				
	return len(no_beacons - beacons)

def search(arr):
    MIN_COORD = 0
    MAX_COORD = 4000000

    for y in range(MIN_COORD, MAX_COORD+1):
        ranges = []
        for (sx, sy, bx, by) in arr:
            min_manhattan = abs(sx-bx) + abs(sy-by)

            dist = abs(sy - y)
            mult = min_manhattan - dist
            if mult < 0:
                continue

            ranges.append((sx - mult, sx + mult))

        ranges.sort()

        compact = []
        low_x, high_x = ranges[0]
        for n_low_x, n_high_x in ranges[1:]:
            if n_low_x-1 <= high_x:
                high_x = max(high_x, n_high_x)
            else:
                compact.append((low_x, high_x))
                low_x, high_x = n_low_x, n_high_x
        compact.append((low_x, high_x))

        if len(compact) != 1:
            assert(len(compact) == 2)
            (a, b), (c, d) = compact
            assert(b+2 == c)
            x = b+1
            return x * 4000000 + y

@timer
@print_result
def exercise2(arr):
	return search(arr)

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	arr = []
	for line in input:
		x = line.split()
		sx = x[2].split("=")[1][:-1]
		sy = x[3].split("=")[1][:-1]
		bx = x[-2].split("=")[1][:-1]
		by = x[-1].split("=")[1]
		arr.append(list(map(int, [sx, sy, bx, by])))
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
