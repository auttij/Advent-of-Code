import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def priority(char):
	if char < 'a':
		return ord(char) - 38
	else:
		return ord(char) - 96

@timer
@print_result
def exercise1(arr):
	l = []
	for line in arr:
		f, s = line[:len(line)//2], line[len(line)//2:]
		common = set(f) & set(s)
		l.append(common.pop())
	return sum(list(map(priority, l)))

@timer
@print_result
def exercise2(arr):
	badges = []
	l = iter(arr)
	for l1, l2, l3 in zip(l, l, l):
		common = set(l1) & set(l2) & set(l3)
		badges.append(common.pop())
	return sum(list(map(priority, badges)))

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
