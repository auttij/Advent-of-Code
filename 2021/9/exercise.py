import sys
sys.path.insert(0,'..')
import helpers

class Mapper():
	def __init__(self, input):
		self.arr = input
		self.xmax = len(input[0])
		self.ymax = len(input)
		self.low_points = []
		self.get_low_points()

	def get_neighbours(self, x, y):
		sur = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)] # surrounding coordinates
		filtered = [i for i in sur if i[0] >= 0 and i[0] < self.xmax and i[1] >= 0 and i[1] < self.ymax]
		return filtered

	def is_low_point(self, x, y):
		val = self.arr[y][x]
		lower = [self.arr[y][x] > val for x, y in self.get_neighbours(x, y)]
		return all(lower)
	
	def get_low_points(self):
		for x in range(self.xmax):
			for y in range(self.ymax):
				if self.is_low_point(x, y):
					self.low_points.append([x, y])

	def visited_arr(self):
		return [[False for i in range(self.xmax)] for j in range(self.ymax)]

	def get_basins(self):
		sizes = []
		for i in self.low_points:
			size = 0
			stack = [i]
			visited = self.visited_arr()
			while len(stack) > 0:
				x, y = stack[-1]
				visited[y][x] = True
				nei = self.get_neighbours(x, y)
				new = False
				for n in nei:
					if not new and not visited[n[1]][n[0]] and int(self.arr[n[1]][n[0]]) < 9:
						stack.append([ n[0], n[1]  ])
						new = True
				if not new:
					stack.pop()
					size += 1
			sizes.append(size)
		return sizes

def exercise1(arr):
	m = Mapper(arr)
	l = m.low_points
	dangers = [int(m.arr[y][x]) for x, y in l]
	return len(dangers) + sum(dangers)

def exercise2(arr):
	m = Mapper(arr)
	basins = m.get_basins()
	b3 = sorted(basins, reverse=True)[:3]
	return b3[0] * b3[1] * b3[2]


if __name__ == "__main__":
	f1 = "input1.txt"
	f2 = "input2.txt"

	filename = f1
	if len(sys.argv) > 1:
		input = sys.argv[1]
		print(input)
		if input == "1":
			filename = f1
		elif input == "2":
			filename = f2

	arr = helpers.read_file_to_arr(filename)
	map = [list(i) for i in arr]
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
