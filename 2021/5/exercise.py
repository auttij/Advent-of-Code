import sys
sys.path.insert(0,'..')
import helpers

"""
Helper class to keep track of a map
"""
class Mapper():
	def __init__(self, arr):
		self.input = arr
		self.get_limits()
		self.map = self.create_arr()

	"""Get max values for y and x from input"""
	def get_limits(self):
		xmax = 0
		ymax = 0
		for pair in self.input:
			x1, y1 = pair[0]
			x2, y2 = pair[1]

			if x1 > xmax:
				xmax = x1
			if x2 > xmax:
				xmax = x2
			if y1 > ymax:
				ymax = y1
			if y2 > ymax:
				ymax = y2
		self.xmax = xmax
		self.ymax = ymax

	"""get coordinates for points on diagonal line"""
	def get_diagonal_points(self, x1, x2, y1, y2):
		start_x, end_x, start_y, end_y = x1, x2, y1, y2
		if start_x > end_x:
			start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y

		result = []
		slope = (end_y - start_y) // (end_x - start_x)
		for i, j in zip(range(start_x, end_x), range(start_y, end_y, slope)):
			result.append([i, j])
		result.append([end_x, end_y])
		return result

	"""Add a line of vents to map 
	param: input -> [[Int, Int], [Int, Int]]
		end coordinates of a line
	param: only_hv -> bool
		Wether or not only horizontal and vertical inputs should be accepted
	"""
	def add_vents(self, input, only_hv=True):
		x1, y1 = input[0]
		x2, y2 = input[1]

		# if only horizontal and vertical lines are allowed (exercise 1), skip those that aren't
		if only_hv and x1 != x2 and y1 != y2:
			return
		if x1 == x2:
			ymin = min(y1, y2)
			ymax = max(y1, y2)
			for y in range(ymin, ymax + 1):
				#print(x1, y)
				self.map[y][x1] += 1
		elif y1 == y2:
			xmin = min(x1, x2)
			xmax = max(x1, x2)
			for x in range(xmin, xmax + 1):
				#print(x, y1)
				self.map[y1][x] += 1
		else:
			# diagonal
			diagonal_points = self.get_diagonal_points(x1, x2, y1, y2)
			#print(f"{(x1, x2)} , {(y1, y2)}")
			#print(diagonal_points)
			for x, y in diagonal_points:
				self.map[y][x] += 1

	"""Create basis for result array"""
	def create_arr(self):
		return [[0 for i in range(self.xmax + 1)] for i in range(self.ymax + 1)]

	"""pretty print a row by row representation of result"""
	def print(self):
		for row in self.map:
			for val in row:
				chr = str(val)
				if val == 0:
					chr = "."
				print(chr, end="")
			print("")

	"""Go through all lines of input and add them to map"""
	def add_all_vents(self, only_hv=True):
		for i in self.input:
			self.add_vents(i, only_hv=only_hv)

	"""Calculate the result => 
	The amount of coordinates where	amount of vents is 2 or more"""
	def result(self):
		res = 0
		for row in self.map:
			for val in row:
				if val >= 2:
					res += 1
		return res

def exercise1(arr):
	m = Mapper(arr)
	m.add_all_vents()
	return m.result()

def exercise2(arr):
	m = Mapper(arr)
	m.add_all_vents(only_hv=False)
	return m.result()

def arr_to_int_pairs(arr):
	new_arr = []
	for i in arr:
		begin, end = i.split(" -> ")
		begin_split = begin.split(",")
		x1, y1 = int(begin_split[0]), int(begin_split[1])
		end_split = end.split(",")
		x2, y2 = int(end_split[0]), int(end_split[1])
		new_arr.append([(x1, y1), (x2, y2)])
	return new_arr

if __name__ == "__main__":
	f1 = "input1.txt"
	f2 = "input2.txt"

	filename = f1
	if len(sys.argv) > 1:
		input = sys.argv[1]
		if input == "1":
			filename = f1
		elif input == "2":
			filename = f2

	arr = helpers.read_file_to_arr(filename)
	new_arr = arr_to_int_pairs(arr)

	result = exercise1(new_arr.copy())
	print(result)
	result = exercise2(new_arr.copy())
	print(result)
