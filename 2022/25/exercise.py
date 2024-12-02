import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def fromSnafu(num):
	a = [n.replace('-', '-1').replace('=', '-2') for n in list(num)]
	b = [int(n, 5) * pow(5, i) for i, n in enumerate(a[::-1])]
	return sum(b)

def toSnafu(num):
	b5 = []
	while num:
		b5.insert(0, num % 5)
		num //= 5

	while any(n >= 3 for n in b5):
		for i in range(len(b5)):
			if b5[i] >= 3:
				b5[i-1] += 1
				b5[i] -= 5
	return "".join(["0","1","2","=","-"][n] for n in b5)

@timer
@print_result
def exercise1(arr):
	ans = sum((fromSnafu(i) for i in arr))
	return toSnafu(ans)

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise1(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
