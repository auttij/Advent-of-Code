import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import combinations
import z3

def parse(data):
	return [((px, py, pz), (vx, vy, vz)) for px, py, pz, vx, vy, vz in data]	

def line_intersection(line1, line2):
	xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])


	def det(a, b):
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)
	if div == 0:
		return None, None

	d = (det(*line1), det(*line2))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div
	return x, y

@timer
@print_result
def part1(input):
	mi = 7
	ma = 27
	
	mi = 200_000_000_000_000
	ma = 400000000000000

	out = 0
	for a, b in combinations(input, 2):
		a, va = a
		b, vb = b

		ap1 = tuple(a[i] + va[i] for i in range(len(a)))
		bp1 = tuple(b[i] + vb[i] for i in range(len(b)))

		x, y = line_intersection((a, ap1), (b, bp1))

		if x is None:
			continue

		dx = x - a[0]
		dy = y - a[1]

		if not ((dx > 0) == (va[0] > 0) and (dy > 0) == (va[1] > 0)):
			continue

		dx = x - b[0]
		dy = y - b[1]
		if not ((dx > 0) == (vb[0] > 0) and (dy > 0) == (vb[1] > 0)):
			continue

		# print(a, va, '|', b, vb, '->', x, y)

		if mi <= x <= ma and mi <= y <= ma:
			out += 1

	return out


@timer
@print_result
def part2(input):
	x, y, z = z3.Reals('x y z')
	vx, vy, vz = z3.Reals('vx vy vz')
	s = z3.Solver()

	for i, (pos, vel) in enumerate(input[:3]):
		x_i, y_i, z_i = pos
		vx_i, vy_i, vz_i = vel
		t_i = z3.Real(f"t_{i}")
		s.add(x_i + vx_i * t_i == x + vx * t_i)
		s.add(y_i + vy_i * t_i == y + vy * t_i)
		s.add(z_i + vz_i * t_i == z + vz * t_i)
		
	s.check()
	m = s.model()
	return m[x].as_long() + m[y].as_long() + m[z].as_long()



def main(args=None):
	data = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
	input = parse(data)
	if isinstance(input, str):
		part1(input)
		part2(input)
	else:
		part1(input.copy())
		part2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
