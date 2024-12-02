import sys
sys.path.insert(0,'..')
import helpers
from functools import lru_cache

@lru_cache(maxsize=64)
def calculate_offspring(counter, days):
	offspring = list(range(counter, days, 7))
	offspring_offspring = [calculate_offspring(9 + i, days) for i in offspring]
	return len(offspring) + sum(offspring_offspring)

def exercise1(arr):
	return len(arr) + sum([calculate_offspring(i, 80) for i in arr])

def exercise2(arr):
	return len(arr) + sum([calculate_offspring(i, 256) for i in arr])

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
