import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

aNum = ord('a')
zNum = ord('z') - aNum
def toNum(input):
	return [ord(x) - aNum for x in input]

def toStr(input):
	return "".join([chr(x + aNum) for x in input])

def increment(input):
	carry = 1
	input_len = len(input) - 1
	for i, val in enumerate(input[::-1]):
		ind = input_len - i
		new_val = val + carry
		if new_val > zNum:
			new_val = 0
		else:
			carry = 0
		input[ind] = new_val
	if carry == 1:
		input.insert(0, 0)
	return input

def increasing_straight(input):
	def condition(chnk):
		return chnk[0] + 1 == chnk[1] and chnk[1] + 1 == chnk[2]
	
	chunks = [input[i : i + 3] for i in range(0, len(input), 1)][:-2]
	return any(list(map(condition, chunks)))

def noILO(input):
	return toNum('i') not in input and toNum('l') not in input and toNum('o') not in input

def repeating_letters(input):
	chunks = [input[i : i + 2] for i in range(0, len(input), 1)][:-1]
	sets = map(set, chunks)
	filtered = [list(i)[0] for i in list(filter(lambda x: len(x) == 1, sets))]
	return len(set(filtered)) >= 2

def check(input):
	return increasing_straight(input) and noILO(input) and repeating_letters(input)

@timer
@print_result
def exercise1(arr):
	num = toNum(arr)
	while not check(num):
		increment(num)
	return toStr(num)

@timer
@print_result
def exercise2(arr):
	num = toNum(arr)
	while not check(num):
		increment(num)
	increment(num)
	while not check(num):
		increment(num)
	return toStr(num)

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str, args)
	exercise1(arr)
	exercise2(arr)

if __name__ == "__main__":
	main(argv[1:])
