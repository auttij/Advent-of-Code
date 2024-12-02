import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def move(H,T):
    dr = (H[0]-T[0])
    dc = (H[1]-T[1])
    if abs(dr)<=1 and abs(dc)<=1:
        # ok
        pass
    elif abs(dr)>=2 and abs(dc)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1]-1 if T[1]<H[1] else H[1]+1)
    elif abs(dr)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1])
    elif abs(dc)>=2:
        T = (H[0], H[1]-1 if T[1]<H[1] else H[1]+1)
    return T


@timer
@print_result
def exercise(arr):
	H = (0,0)
	T = [(0,0) for _ in range(9)]
	DR = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
	DC = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
	P1 = set([T[0]])
	P2 = set([T[8]])
	for line in arr:
		d,amt = line.split()
		amt = int(amt)
		for _ in range(amt):
			H = (H[0] + DR[d], H[1]+DC[d])
			T[0] = move(H, T[0])
			for i in range(1, 9):
				T[i] = move(T[i-1], T[i])
			P1.add(T[0])
			P2.add(T[8])
	print(len(P1))
	print(len(P2))




def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise(arr)

if __name__ == "__main__":
	main(argv[1:])
