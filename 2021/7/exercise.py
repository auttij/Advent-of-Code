import sys
sys.path.insert(0,'..')
import helpers

def fuel(arr, pos):
	return sum([abs(pos-i) for i in arr])
	
def exercise1(arr):
	m = max(arr)
	a = [fuel(arr, i) for i in range(m + 1)]
	return min(a)

def fuel2(arr, pos):
	return int(sum([(abs(pos-i) + 1) * abs(pos - i)/2 for i in arr]))

def exercise2(arr):
	m = max(arr)
	a = [fuel2(arr, i) for i in range(m + 1)]
	return min(a)

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
	new_arr = [int(i) for i in arr[0].split(",")]
	result = exercise1(new_arr.copy())
	print(result)
	result = exercise2(new_arr.copy())
	print(result)
