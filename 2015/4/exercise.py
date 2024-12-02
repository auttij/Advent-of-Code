import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
import hashlib

@timer
@print_result
def exercise1(arr):
	i = 0
	while True:
		s = arr + str(i)
		result = hashlib.md5(s.encode())
		if result.hexdigest()[:5] == '00000':
			return i
		else:
			i += 1

@timer
@print_result
def exercise2(arr):
	i = 0
	while True:
		if i % 1000000 == 0:
			print(i, end="\r")
		result = hashlib.md5(f"{arr + str(i)}".encode())
		if result.hexdigest()[:6] == '000000':
			return i
		i += 1

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str, args)
	exercise1(arr)
	exercise2(arr)

if __name__ == "__main__":
	main(argv[1:])
