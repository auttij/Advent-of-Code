import sys
sys.path.insert(0,'..')
import helpers

def exercise1(arr):
	outputs = [i.split("|")[1] for i in arr]
	count = 0
	for output in outputs:
		for num in output.split(" "):
			if len(num) in [2, 3, 4, 7]:
				count += 1
	return count

class Translator():
	def __init__(self, mapping, out):
		self.input_mapping = mapping
		self.map = {}
		self.rev_map = {}
		self.out = out
		self.create_mapping()

	def create_mapping(self):
		for i in self.input_mapping:
			if len(i) == 2:
				self.map[i] = "1"
			elif len(i) == 3:
				self.map[i] = "7"
				self.rev_map["7"] = i
			elif len(i) == 4:
				self.map[i] = "4"
				self.rev_map["4"] = i
			elif len(i) == 7:
				self.map[i] = "8"

		input = [i for i in self.input_mapping if i not in self.map.keys()]
		# 6 and 9
		# 6 shares 2 segments with 7, 9 shares 3 segments with 7
		for i in input:
			if len(i) == 6:
				common_w7 = ''.join(set(i).intersection(self.rev_map["7"]))
				common_w4 = ''.join(set(i).intersection(self.rev_map["4"]))
				if len(common_w7) == 2:
					self.map[i] = "6"
				elif len(common_w7) == 3:
					if len(common_w4) == 4:
						self.map[i] = "9"
					elif len(common_w4) == 3:
						self.map[i] = "0"

		input = [i for i in self.input_mapping if i not in self.map.keys()]
		# 2, 3, 5 left. 3 shares 3 with 7
		for i in input:
			common_w7 = ''.join(set(i).intersection(self.rev_map["7"]))
			if len(common_w7) == 3:
				self.map[i] = "3"

		input = [i for i in self.input_mapping if i not in self.map.keys()]
		# 2 & 5 left. 2 shares 2 with 4, 5 shares 3
		for i in input:
			common_w4 = ''.join(set(i).intersection(self.rev_map["4"]))
			if len(common_w4) == 3:
				self.map[i] = "5"
			elif len(common_w4) == 2:
				self.map[i] = "2"

	def decode_output(self):
		return int("".join([self.map[i] for i in self.out]))

def exercise2(arr):
	out = []
	for row in arr:
		mapping, output = row.split("|")
		map_arr = ["".join(sorted(i)) for i in mapping.split()]
		out_arr = ["".join(sorted(i)) for i in output.split()]
		t = Translator(map_arr, out_arr)
		out.append(t.decode_output())
	return sum(out)

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
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
