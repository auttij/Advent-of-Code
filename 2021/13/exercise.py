import sys
sys.path.insert(0,'..')
import helpers
from itertools import takewhile, dropwhile

def folded_coord(fold_point, val):
	return fold_point - (val - (fold_point))

def fold(x, y, horizontal, line):
	if horizontal:
		if y >= line:
			return (x, folded_coord(line, y))
	else:
		if x >= line:
			return (folded_coord(line, x), y)
	return (x, y)

def fold_all_coords(coords, xy, line):
	horizontal = xy == "y"
	result = []
	for x, y in coords:
		folded = fold(x, y, horizontal, line)
		result.append(folded)
	return list(set(result))

def print_arr(arr):
	max_x = 0
	max_y = 0
	for x,y in arr:
		if x > max_x:
			max_x = x
		if y > max_y:
			max_y = y
	
	res = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
	for x, y in arr:
		res[y][x] = "#"
	for line in res:
		print("".join(line))

def exercise1(arr, arr_inst):
	split_instructions = [i[0].split(" ")[-1].split("=") for i in arr_inst]
	instructions = [[x, int(i)] for x, i in split_instructions]
	#print_arr(arr)
	for xy, line in [instructions[0]]:
		arr = fold_all_coords(arr, xy, line)
		
		#print_arr(arr)

	return len(set(arr))

def exercise2(arr, arr_inst):
	split_instructions = [i[0].split(" ")[-1].split("=") for i in arr_inst]
	instructions = [[x, int(i)] for x, i in split_instructions]
	for xy, line in instructions:
		arr = fold_all_coords(arr, xy, line)
	print_arr(arr)
	return len(set(arr))

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
	split = [i.split(",") for i in arr]
	coords = list(takewhile(lambda x: len(x) > 1, split))
	new_arr = [(int(x), int(y)) for x, y in coords]

	instructions = list(dropwhile(lambda x: len(x) > 1, split))[1:]



	result = exercise1(new_arr.copy(), instructions.copy())
	print(result)
	result = exercise2(new_arr.copy(), instructions.copy())
	print(result)
