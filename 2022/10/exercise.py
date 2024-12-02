import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def updateSignal(signal, cycle, x):
	if (cycle % 40) == 20:
		return signal + (cycle * x)
	return signal

@timer
@print_result
def exercise1(arr):
	cycle = 0
	X = 1
	signal = 0
	for line in arr:
		cmd = line.split()
		if cmd[0] == "noop":
			cycle += 1
			signal = updateSignal(signal, cycle, X)
			continue
		if cmd[0] == 'addx':
			amt = int(cmd[1])
			cycle += 1
			signal = updateSignal(signal, cycle, X)
			cycle += 1 
			signal = updateSignal(signal, cycle, X)
			X += amt

	return signal


def checkPos(c, x):
	cycle = c % 40
	if cycle % 40 == x:
		return x
	elif x < 239 and cycle == x + 1:
		return x + 1
	elif x < 238 and cycle == x + 2:
		return x + 2
	return -1
	
def draw(out, pos, cycle):
	if pos == -1:
		return out
	out[cycle // 40][cycle % 40] = '#'
	return out

@timer
@print_result
def exercise2(arr):
	out = [['.' for i in range(40)] for j in range(6)]
	cycle = 0
	X = 1
	for line in arr:
		cmd = line.split()
		if cmd[0] == "noop":
			cycle += 1
			pos = checkPos(cycle, X)
			out = draw(out, pos, cycle)
			continue
		if cmd[0] == 'addx':
			amt = int(cmd[1])
			cycle += 1
			pos = checkPos(cycle, X)
			out = draw(out, pos, cycle)
			cycle += 1 
			pos = checkPos(cycle, X)
			out = draw(out, pos, cycle)
			X += amt
	for line in out:
		print("".join(line))

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
