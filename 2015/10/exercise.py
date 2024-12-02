import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def iterate(input, iterations):
	s = input
	for _ in range(iterations):
		# print(s)
		new = []
		cur = s[0]
		curCount = 0
		ind = 0
		while ind < len(s):
			# print(ind, s[ind], curCount)
			if s[ind] == cur:
				curCount += 1
			else:
				new.extend([str(curCount), cur])
				cur = s[ind]
				curCount = 1
			ind += 1
		new.extend([str(curCount), cur])
		s = "".join(new)
	# print(s)
	return len(s)

@timer
@print_result
def exercise1(input):
	return iterate(input, 40)
			

@timer
@print_result
def exercise2(input):
	return iterate(input, 50)

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str, args)
	exercise1(arr[::])
	exercise2(arr[::])

if __name__ == "__main__":
	main(argv[1:])
