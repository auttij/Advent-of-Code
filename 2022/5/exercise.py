import logging, re
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(boxes, numbers):
	for c, frm, to in numbers:
		for _ in range(c):
			boxes[to].append(boxes[frm].pop(-1))
	return "".join(z[-1] for z in boxes[1:])

@timer
@print_result
def exercise2(boxes, numbers):
	for c, frm, to in numbers:
		boxes[to].extend(boxes[frm][-c:])
		del boxes[frm][-c:]
	return "".join(z[-1] for z in boxes[1:])

def tupler(lines):
	return [list(map(int, re.findall(r'\d+', line))) for line in lines.split("\n")]

def main(args=None):
	s = init(path.dirname(__file__), inputs.read_to_str, args)
	numbers = tupler(s.split("\n\n")[1])

	boxes = [
		[],
		list("DLJRVGF"),
		list("TPMBVHJS"),
		list("VHMFDGPC"),
		list("MDPNGQ"),
		list("JLHNF"),
		list("NFVQDGTZ"),
		list("FDBL"),
		list("MJBSVDN"),
		list("GLD")
	]
	exercise1(boxes, numbers)

	boxes = [
		[],
		list("DLJRVGF"),
		list("TPMBVHJS"),
		list("VHMFDGPC"),
		list("MDPNGQ"),
		list("JLHNF"),
		list("NFVQDGTZ"),
		list("FDBL"),
		list("MJBSVDN"),
		list("GLD")
	]
	exercise2(boxes, numbers)

if __name__ == "__main__":
	main(argv[1:])
