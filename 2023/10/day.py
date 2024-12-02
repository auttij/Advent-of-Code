import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import defaultdict, deque


# east south west north
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
happy = ["-7J", "|LJ", "-FL", "|F7"]
transform = {
	(0,"-"): 0,
	(0,"7"): 1,
	(0,"J"): 3,
	(1,"|"): 1,
	(1,"L"): 0,
	(1,"J"): 2,
	(2,"-"): 2,
	(2,"F"): 1,
	(2,"L"): 3,
	(3,"|"): 3,
	(3,"F"): 0,
	(3,"7"): 2,
}

def get_start_pos_and_dirs(G):
	W = len(G[0])
	H = len(G)
	sx, sy = -1, -1
	for y, R in enumerate(G):
		for x, c in enumerate(R):
			if c == "S":
				sx = x
				sy = y
				break

	start_dirs = []
	for i in range(4):
		pos = dirs[i]
		by = sy+pos[0]
		bx = sx+pos[1]
		if 0<=bx<=W and 0<=by<=H and G[by][bx] in happy[i]:
			start_dirs.append(i)
	return sy, sx, start_dirs


@timer
@print_result
def part1(G):
	sy, sx, start_dirs = get_start_pos_and_dirs(G)

	curdir = start_dirs[0]
	cy = sy + dirs[curdir][0]
	cx = sx + dirs[curdir][1]
	dist = 1
	while (cy, cx) != (sy, sx):
		dist += 1
		curdir = transform[(curdir,G[cy][cx])]
		cy = cy + dirs[curdir][0]
		cx = cx + dirs[curdir][1]
	return dist//2


@timer
@print_result
def part2(G):
	W = len(G[0])
	H = len(G)
	O = [[0]*W for _ in range(H)]
	sy, sx, start_dirs = get_start_pos_and_dirs(G)
	start_valid = 3 in start_dirs
	
	O[sy][sx] = 1
	curdir = start_dirs[0]
	cy = sy + dirs[curdir][0]
	cx = sx + dirs[curdir][1]
	while (cy, cx) != (sy, sx):
		O[cy][cx] = 1
		curdir = transform[(curdir,G[cy][cx])]
		cy = cy + dirs[curdir][0]
		cx = cx + dirs[curdir][1]
	
	ct = 0
	for i in range(H):
		inn = False
		for j in range(W):
			if O[i][j]:
				if G[i][j] in "|JL" or (G[i][j]=="S" and start_valid): 
					inn = not inn
			else:
				ct += inn
	return ct

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	if isinstance(input, str):
		part1(input)
		part2(input)
	else:
		part1(input.copy())
		part2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
