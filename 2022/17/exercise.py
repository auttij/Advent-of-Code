import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from math import ceil
from collections import defaultdict


def getPiece(t, y):
    if t==0:
        return set([(2,y), (3,y), (4,y), (5,y)])
    elif t == 1:
        return set([(3, y+2), (2, y+1), (3,y+1), (4,y+1), (3,y)])
    elif t == 2:
        return set([(2, y), (3,y), (4,y), (4,y+1), (4,y+2)])
    elif t==3:
        return set([(2,y),(2,y+1),(2,y+2),(2,y+3)])
    elif t==4:
        return set([(2,y+1),(2,y),(3,y+1),(3,y)])
    else:
        assert False

def moveLeft(piece):
    if any([x==0 for (x,y) in piece]):
        return piece
    return set([(x-1,y) for (x,y) in piece])

def moveRight(piece):
    if any([x==6 for (x,y) in piece]):
        return piece
    return set([(x+1,y) for (x,y) in piece])

def moveDown(piece):
    return set([(x,y-1) for (x,y) in piece])

def moveUp(piece):
    return set([(x,y+1) for (x,y) in piece])


def show(R):
    maxY = max([y for (x,y) in R])
    for y in range(maxY,0,-1):
        row = ''
        for x in range(7):
            if (x,y) in R:
                row += '#'
            else:
                row += ' '
        print(row)

# Get signature => pattern of rocks from last X rows
def signature(R, maxY):
    return frozenset([(x, maxY - y) for (x, y) in R if maxY - y <= 15])

def iterate(jets, rounds):
	R = set([(x,0) for x in range(7)])
	
	SEEN = {}
	top = 0
	i = 0
	t = 0
	added = 0

	while t < rounds:
		piece = getPiece(t%5, top+4)
		while True:

			# move and if collision, move back
			if jets[i] == '<':
				piece = moveLeft(piece)
				if piece & R:
					piece = moveRight(piece)
			else:
				piece = moveRight(piece)
				if piece & R:
					piece = moveLeft(piece)
			i = (i + 1) % len(jets)


			piece = moveDown(piece)

			# collision with previously placed pieces
			if piece & R:
				piece = moveUp(piece)
				R |= piece # place

				cMax = max([y for (x, y) in piece])
				if cMax > top:
					top = cMax

				SR = (i, t%5, signature(R, top))
				if SR in SEEN:
					(oldt, oldy) = SEEN[SR]
					dy = top - oldy # change in y with cycle
					dt = t - oldt   # change in time
					amt = (rounds - t) // dt	# repetitions
					added += amt * dy 	# added y height 
					t += amt * dt 		# added time
					assert t <= rounds
				SEEN[SR] = (t,top)
				# show(R)
				break
		t += 1
	# print(len(SEEN))
	return top + added

@timer
@print_result
def exercise1(arr):
	return iterate(arr, 2022)

@timer
@print_result
def exercise2(arr):
	return iterate(arr, 1_000_000_000_000)

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str, args)

	exercise1(arr[::])
	exercise2(arr[::])

if __name__ == "__main__":
	main(argv[1:])
