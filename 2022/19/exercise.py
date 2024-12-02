import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import deque



def solve(Co, Cc, Co1, Co2, Cg1, Cg2, T):
    best = 0
    # state is (ore, clay, obsidian, geodes, r1, r2, r3, r4, time)
    S = (0, 0, 0, 0, 1, 0, 0, 0, T)
    Q = deque([S])
    SEEN = set()
    while Q:
        state = Q.popleft()
        #print(state)
        o,c,ob,g,r1,r2,r3,r4,t = state

        best = max(best, g)
        if t==0:
            continue

        Core = max([Co, Cc, Co1, Cg1])
        if r1>=Core:
            r1 = Core
        if r2>=Co2:
            r2 = Co2
        if r3>=Cg2:
            r3 = Cg2
        if o >= t*Core-r1*(t-1):
            o = t*Core-r1*(t-1)
        if c>=t*Co2-r2*(t-1):
            c = t*Co2 - r2*(t-1)
        if ob>=t*Cg2-r3*(t-1):
            ob = t*Cg2-r3*(t-1)

        state = (o,c,ob,g,r1,r2,r3,r4,t)

        if state in SEEN:
            continue
        SEEN.add(state)

        if len(SEEN) % 1000000 == 0:
            print(t,best,len(SEEN))
        assert o>=0 and c>=0 and ob>=0 and g>=0, state
        Q.append((o+r1,c+r2,ob+r3,g+r4,r1,r2,r3,r4,t-1))
        if o>=Co: # buy ore
            Q.append((o-Co+r1, c+r2, ob+r3, g+r4, r1+1,r2,r3,r4,t-1))
        if o>=Cc:
            Q.append((o-Cc+r1, c+r2, ob+r3, g+r4, r1,r2+1,r3,r4,t-1))
        if o>=Co1 and c>=Co2:
            Q.append((o-Co1+r1, c-Co2+r2, ob+r3, g+r4, r1,r2,r3+1,r4,t-1))
        if o>=Cg1 and ob>=Cg2:
            Q.append((o-Cg1+r1, c+r2, ob-Cg2+r3, g+r4, r1,r2,r3,r4+1,t-1))
    return best

@timer
@print_result
def exercise1(arr):
	out = 0
	for line in arr:
		b, *prices = line
		val = solve(*prices, 24)
		out += val * b
	return out

@timer
@print_result
def exercise2(arr):
	out = 1
	for line in arr[:3]:
		b, *prices = line
		val = solve(*prices, 32)
		out *= val
	return out

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
