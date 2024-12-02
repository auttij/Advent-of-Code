import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def parse_input(s):
    for idx, line in enumerate(s, start=1):
        a, b = line.split('~')
        a = tuple(map(int, a.split(',')))
        b = tuple(map(int, b.split(',')))
        yield a, b, idx

def generate_bricks(data):
	bricks = []

	for (x0, y0, z0), (x1, y1, z1), _ in data:
		b = set()
		for x in range(x0, x1+1):
			for y in range(y0, y1+1):
				# Only the bottom and top row are needed
				for z in set([z0, z1]):
					b.add((x,y,z))

		bricks.append(b)
	return bricks

@timer
@print_result
def part1(input):
	data = sorted(parse_input(input), key=lambda brick: brick[0][2])
	bricks = generate_bricks(data)
	
	settled_positions = set()
	unsettled_positions = set()

	for b in bricks:
		unsettled_positions |= b

	def fall(b):
		while True:
			new_b = set()
			for x,y,z in b:
				new_b.add((x,y,z-1))
			assert(len(new_b & unsettled_positions) == 0)
			if len(new_b & settled_positions) != 0:
				return b # Settled
			if min(z for x,y,z in new_b) <= 0:
				return b # Settled
			b = new_b

	for i, b in enumerate(bricks):
		unsettled_positions -= b

		b = fall(b)
		settled_positions |= b
		bricks[i] = b

	answer = 0

	for idx, b in enumerate(bricks):
		settled_positions -= b

		was_safe = True
		tested = []
		for i2, b2 in enumerate(bricks[idx+1:]):
			tested.append(idx+1+i2)
			settled_positions -= b2
			if fall(b2) != b2:
				was_safe = False
				settled_positions |= b2
				break
			settled_positions |= b2

		if was_safe:
			answer += 1

		settled_positions |= b
	return answer
	

@timer
@print_result
def part2(input):
	data = sorted(parse_input(input), key=lambda brick: brick[0][2])
	bricks = generate_bricks(data)

	settled_positions = set()
	unsettled_positions = set()

	for b in bricks:
		unsettled_positions |= b
		test = len(b)

	def fall(b):
		while True:
			new_b = set()
			for x,y,z in b:
				new_b.add((x,y,z-1))
			assert(len(new_b & unsettled_positions) == 0)
			if len(new_b & settled_positions) != 0:
				return b # Settled
			if min(z for x,y,z in new_b) <= 0:
				return b # Settled
			b = new_b

	for idx, b in enumerate(bricks):
		unsettled_positions -= b

		b = fall(b)
		settled_positions |= b
		bricks[idx] = b

	answer = 0

	for idx, b in enumerate(bricks):
		old_settled = set(settled_positions)

		settled_positions -= b

		for i2, b2 in enumerate(bricks[idx+1:], start=idx+1):
			settled_positions -= b2
			new_b2 = fall(b2)
			if b2 != new_b2:
				answer += 1
			settled_positions |= new_b2

		# Restore
		settled_positions = old_settled
	return answer


def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	part1(input.copy())
	part2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
