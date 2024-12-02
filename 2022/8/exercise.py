import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def los(arr, r, c):
	l = []
	if r > 0:
		l1 = []
		ri1 = r
		while ri1 > 0:
			ri1 -= 1
			l1.append(arr[c][ri1])
		l.append(l1)
		
	if c > 0:
		l2 = []
		ci2 = c
		while ci2 > 0:
			ci2 -= 1
			l2.append(arr[ci2][r])
		l.append(l2)

	if r + 1 < len(arr[0]): 
		l3 = []
		ri3 = r
		while ri3 + 1 < len(arr[0]):
			ri3 += 1
			l3.append(arr[c][ri3])
		l.append(l3)
		
	if c + 1 < len(arr): 
		l4 = []
		ci4 = c
		while ci4 + 1 < len(arr[0]):
			ci4 += 1
			l4.append(arr[ci4][r])
		l.append(l4)
	return l



@timer
@print_result
def exercise1(arr):
	count = 0
	for c, l in enumerate(arr):
		for r, v in enumerate(l):
			if (r == 0 or c == 0 or r == len(arr[0]) - 1 or c == len(arr) - 1):
				count += 1
			else:
				nei = los(arr, r, c)
				neimapped = []
				for nei2 in nei:
					neimapped.append(all([i < v for i in nei2]))

				if (any(neimapped)):
					count += 1
	return count


def score(arr, r, c, v):
	nei = los(arr, r, c)
	lens = []
	if len(nei) < 4:
		lens.append(0)

	for l in nei:
		n = []
		while len(l) > 0:
			n.append(l.pop(0))
			if n[-1] >= v:
				break
		lens.append(len(n))

	result = 1
	for x in lens:
		result *= x
	return result
		
	

@timer
@print_result
def exercise2(arr):
	top = 0
	for c, l in enumerate(arr):
		for r, v in enumerate(l):
			if c == 0 or r == 0 or c == len(arr) - 1 or r == len(arr) -  1:
				continue
			s = score(arr, r, c, v)
			if s > top:
				top = s
	return top


def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise1([list(map(int, i)) for i in map(list, arr)])
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
