import sys
sys.path.insert(0,'..')
import helpers

def swap(i):
	if i == "0":
		return "1"
	elif i == "1":
		return "0"

def calculate_ge(arr):
	l = len(arr[0])
	ans = ["1" if sum(map(int, i)) >= l/2 else "0" for i in arr]
	gamma = "".join(ans)
	epsilon = "".join([swap(i) for i in ans])
	return gamma, epsilon

def exercise1(arr):
	new_arr = [list(i) for i in arr]
	trans = helpers.transpose(new_arr)
	gamma, epsilon = calculate_ge(trans)
	return int(gamma, 2) * int(epsilon, 2)

def calc_common(arr):
	l = len(arr)
	s = sum([int(i) for i in arr])
	if s >= l/2:
		return "1"
	else:
		return "0"

def calc_uncommon(arr):
	l = len(arr)
	s = sum([int(i) for i in arr])
	if s < l/2:
		return "1"
	else:
		return "0"


def exercise2(arr):
	new_arr = [list(i) for i in arr]
	oxy_arr = new_arr[::]
	co2_arr = new_arr[::]
	for i in range(len(new_arr[0])):
		if len(oxy_arr) == 1 and len(co2_arr) == 1:
			break
		if len(oxy_arr) > 1:
			oxy_trans = helpers.transpose(oxy_arr)
			common = calc_common(oxy_trans[i])
			oxy_arr = [j for j in oxy_arr if j[i] == common]
		if len(co2_arr) > 1:
			co2_trans = helpers.transpose(co2_arr)
			common = calc_uncommon(co2_trans[i])
			co2_arr = [j for j in co2_arr if j[i] == common]

	return int("".join(oxy_arr[0]), 2) * int("".join(co2_arr[0]), 2)

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

	print(filename)
	arr = helpers.read_file_to_arr(filename)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
