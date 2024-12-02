import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from time import perf_counter

class Node:
	def __init__(self, value, prev=None, next=None):
		self.value = value
		self.prev = prev
		self.next = next

	def __repr__(self):
		return f"{self.value}"

def solve(iterations, dkey, arr):
	r = [Node(i * dkey) for i in arr]
	
	for a,b in zip(r,r[1:]):
		a.next = b
		b.prev = a

	r[-1].next = r[0]
	r[0].prev = r[-1]

	for _ in range(iterations):	
		for x in r:
			x.prev.next = x.next
			x.next.prev = x.prev
			a,b = x.prev, x.next
			move = x.value % (len(r) - 1)		
			for _ in range(move):
				a=a.next
				b=b.next
			a.next = x
			x.prev = a
			b.prev = x
			x.next = b

	for x in r:
		if x.value == 0:
			out = 0
			y = x
			for _ in range(3):
				for _ in range(1000):
					y = y.next
				# print(y.value)
				out += y.value
			return out

@timer
@print_result
def exercise1(arr):
	return solve(1, 1, arr)

@timer
@print_result
def exercise2(arr):
	return solve(10, 811589153, arr)

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_int_arr, args)
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
