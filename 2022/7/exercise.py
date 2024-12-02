import logging
from sys import argv
import os
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


dirs = {}
subdirs = {}

def dirsize(dirname):
    dsize = dirs[dirname]
    for i in subdirs[dirname]:
        if i in dirs:
            dsize += dirsize(i)
    return dsize

@timer
@print_result
def exercise1(dirs):
	totsize = 0
	# part 1
	for d in dirs:
		dsize = dirsize(d)
		if dsize <= 100000:
			totsize += dsize
	return totsize

@timer
@print_result
def exercise2(dirs):
	totsize = dirsize('/')
	unused = 70000000 - totsize
	ms = None
	for d in dirs:
		ds = dirsize(d)
		if unused + ds >= 30000000:
			if ms is None or ms > ds:
				ms = ds
	return ms

@timer
def main(args=None):
	arr = init(os.path.dirname(__file__), inputs.read_to_str_arr, args)
	i = 0
	curdir = None
	for line in arr:
		if len(line.strip()) == 0: continue
		if line[0] == '$':
			c, cmd, *args = line.split()
			if cmd == 'cd':
				path ,= args
				if path[0] == '/':
					curdir = path
				else:
					curdir = os.path.normpath(os.path.join(curdir, path))
				if curdir not in dirs:
					dirs[curdir] = 0
					subdirs[curdir] = []
		else:
			sz, fname = line.split()
			if sz != 'dir':
				dirs[curdir] += int(sz)
			else:
				subdirs[curdir].append(os.path.normpath(os.path.join(curdir, fname)))

	exercise1(dirs)
	exercise2(dirs)

if __name__ == "__main__":
	main(argv[1:])
