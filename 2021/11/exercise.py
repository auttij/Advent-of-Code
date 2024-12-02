import sys
sys.path.insert(0,'..')
import helpers

class Octopus():
	def __init__(self, val, x, y):
		self.val = val
		self.flashed = False
		self.x = x
		self.y = y

	def loc(self):
		return self.x, self.y

	def increment(self):
		self.val += 1
		if self.val > 9 and not self.flashed:
			self.flashed = True
			return True
		return False

	def reset(self):
		if self.flashed:
			self.val = 0
			self.flashed = False

	def __repr__(self):
		return str(self.val)

class Octopi():
	def __init__(self, arr):
		self.xmax = len(arr[0])
		self.ymax = len(arr)
		self.arr = self.create_octopus_arr(arr)

	def total(self):
		return len(self.all_octopi())

	def all_octopi(self):
		return [item for sublist in self.arr for item in sublist]

	def create_octopus_arr(self, arr):
		octopi = []
		for y, row in enumerate(arr):
			new_row = []
			for x, num in enumerate(row):
				new_row.append(Octopus(num, x, y))
			octopi.append(new_row)
		return octopi

	def get_neighbours(self, x, y):
		sur = []
		for nx in range(x-1, x+2):
			for ny in range(y-1, y+2):
				if nx != x or ny != y:
					sur.append([nx, ny])
		filtered = [i for i in sur if i[0] >= 0 and i[0] < self.xmax and i[1] >= 0 and i[1] < self.ymax]
		return filtered

	def turn(self):
		count = 0
		stack = []
		for octopi in self.all_octopi():
			if octopi.increment():
				count += 1
				x, y = octopi.loc()
				for n in self.get_neighbours(x, y):
					no = self.arr[n[1]][n[0]]
					stack.append(no)

		while len(stack) > 0:
			octopi = stack.pop()
			if octopi.increment():
				count += 1
				x, y = octopi.loc()
				for n in self.get_neighbours(x, y):
					no = self.arr[n[1]][n[0]]
					stack.append(no)
		
		for octopi in self.all_octopi():
			octopi.reset()
		return count
	
	def pp(self):
		for row in self.arr:
			for i in row:
				print(i, end="")
			print("")

def exercise1(arr):
	o = Octopi(arr)
	total = 0
	#print(o.pp())
	for i in range(100):
		print(f"turn {i}", end='\r')
		count = o.turn()
		total += count
	#print(o.pp())
	return total

def exercise2(arr):
	o = Octopi(arr)
	total = o.total()
	for i in range(1000):
		print(f"turn {i}", end='\r')
		count = o.turn()
		if count == total:
			return i + 1

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
	new_arr = [list(map(int, list(i))) for i in arr]
	result = exercise1(new_arr.copy())
	print()
	print(result)
	result = exercise2(new_arr.copy())
	print()
	print(result)
