filepath = "./input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def exercise1(arr):
	count = 0
	for i, elem in enumerate(arr[1:]):
		if arr[i] < elem:
			count += 1
	return count

def exercise2(arr):
	def slide(i):
		return sum(arr[i-3:i])
	new_arr = [slide(i + 3) for i, e in enumerate(arr[2:])]
	return exercise1(new_arr)

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	arr = [int(i) for i in arr]
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)

