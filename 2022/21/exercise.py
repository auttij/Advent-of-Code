import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(dict):
	def solve(key):
		val = dict[key]
		
		# print(key, val, len(val))
		if len(val) == 1:
			return int(val[0])
		
		key1, op, key2 = val

		if op == '+':
			return solve(key1) + solve(key2)
		elif op == "-":
			return solve(key1) - solve(key2)
		elif op == "/":
			return solve(key1) / solve(key2)
		elif op == "*":
			return solve(key1) * solve(key2)
		else:
			assert(False)

	return int(solve("root"))

@timer
@print_result
def exercise2(dict):
	dict["root"][1] = "="

	def solve(key):
		val = dict[key]
		if len(val) == 1:
			return int(val[0])
		
		key1, op, key2 = val
		if op == "=":
			v2 = solve(key2)
			v1 = solve(key1)
			return v1 - v2
		
		if op == '+':
			return solve(key1) + solve(key2)
		elif op == "-":
			return solve(key1) - solve(key2)
		elif op == "/":
			return solve(key1) / solve(key2)
		elif op == "*":
			return solve(key1) * solve(key2)
		else:
			assert(False)
	
	lo = 100000000000
	hi = 10000000000000
	while lo < hi:
		m = (lo + hi) // 2
		dict["humn"][0] = m
		diff = solve("root")
		if diff > 0:
			lo = m + 1
		elif diff < 0:
			hi = m - 1
		else:
			return m
	return lo

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	dict = {}
	for line in arr:
		a, *rest = line.split(": ")
		op = rest[0].split(" ")
		if len(op) == 1:
			dict[a] = op
			continue
		dict[a] = op
	exercise1(dict.copy())
	exercise2(dict.copy())

if __name__ == "__main__":
	main(argv[1:])
