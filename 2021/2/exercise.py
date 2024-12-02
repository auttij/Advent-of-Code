def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

class Sub():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.aim = 0

	def read_instruction1(self, instruction):
		num = int(instruction.split(" ")[-1])
		if 'forward' in instruction:
			self.x += num
		if 'up' in instruction:
			self.y -= num
		if 'down' in instruction:
			self.y += num

	def read_instruction2(self, instruction):
		num = int(instruction.split(" ")[-1])
		if 'forward' in instruction:
			self.x += num
			self.y += num * self.aim
		if 'up' in instruction:
			self.aim -= num
		if 'down' in instruction:
			self.aim += num

	def result(self):
		return self.x * self.y

def exercise1(arr):
	s = Sub()
	[s.read_instruction1(i) for i in arr]
	return s.result()

def exercise2(arr):
	s = Sub()
	[s.read_instruction2(i) for i in arr]
	return s.result()
	pass

if __name__ == "__main__":
	filepath = "input2.txt"
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
