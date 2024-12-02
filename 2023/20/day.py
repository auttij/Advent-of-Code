import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import repeat
import math

class Flipflop:
	def __init__(self, name, output):
		self.name = name
		self.power = False
		self.outputs = output

	def __repr__(self):
		return f"%{self.name} -> {", ".join(self.outputs)}"

	def trigger(self, high):
		if high:
			return None
		self.power = not self.power
		if self.power:
			return list(zip(repeat(self.name), repeat(True), self.outputs))
		return list(zip(repeat(self.name), repeat(False), self.outputs))

class Conjuction:
	def __init__(self, name, output):
		self.name = name
		self.power = False
		self.outputs = output
		self.inputs = {}

	def __repr__(self):
		return f"&{self.name} -> {", ".join(self.outputs)}"

	def add_input(self, name):
		self.inputs[name] = False

	def trigger(self, name, high):
		self.inputs[name] = high
		if all(self.inputs.values()): 
			return list(zip(repeat(self.name), repeat(False), self.outputs))
		return list(zip(repeat(self.name), repeat(True), self.outputs))

@timer
@print_result
def part1(flip, conj, broad):
	lows = 0
	highs = 0
	for _ in range(1000):
		queue = list(zip(repeat("button"), repeat(False), broad))
		lows += 1
		while len(queue) > 0:
			top = queue.pop(0)
			src, high, key = top
			if high:
				highs += 1
			else:
				lows += 1

			if key in flip:
				out = flip[key].trigger(high)
				if out:
					queue += out

			if key in conj:
				out = conj[key].trigger(src, high)
				if out:
					queue += out

			# print(top)
	print(lows, highs)
	return lows * highs

@timer
@print_result
def part2(flip, conj, broad):
	seen = { 'xc' : [], 'th': [], 'pd': [], 'bp': []}
	for iter in range(10000):
		queue = list(zip(repeat("button"), repeat(False), broad))
		while len(queue) > 0:
			top = queue.pop(0)
			src, high, key = top
			if src in ['xc', 'th', 'pd', 'bp'] and high:
				seen[src].append(iter + 1)

			if key in flip:
				out = flip[key].trigger(high)
				if out:
					queue += out

			if key in conj:
				out = conj[key].trigger(src, high)
				if out:
					queue += out

	cycles = []
	for v in seen.values():
		v2 = []
		for i in range(len(v) - 1):
			v2.append(v[i + 1] - v[i])
		cycles.append(v2[0])
	return math.lcm(*cycles)


def parse(data):
	flip = {}
	conj = {}
	broad = []

	for line in data:
		start, rest = line.split("->")
		outp = [i.strip() for i in rest.split(",")]
		name = start[1:].strip()
		if start[0] == '%':
			flip[name] = Flipflop(name, outp)
		elif start[0] == '&':
			conj[name] = Conjuction(name, outp)
		else:
			broad = outp
	
	for key in flip:
		f = flip[key]
		outputs = f.outputs
		for o in outputs:
			if o in conj:
				conj[o].add_input(key)
				
	return flip, conj, broad

def main(args=None):
	data = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	flip, conj, broad = parse(data)
	part1(flip, conj, broad)
	part2(flip, conj, broad)

if __name__ == "__main__":
	main(argv[1:])
