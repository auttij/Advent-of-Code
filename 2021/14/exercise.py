import sys
sys.path.insert(0,'..')
import helpers
from collections import Counter

def get_pairs(template):
	return ["".join(i) for i in zip(template[:-1], template[1:])]

def generate_string(pairs, arr):
	out = ""
	for pair in pairs:
		out = out + pair[0] + arr[pair]
	return out + pairs[-1][1]

def calculate_string(template):
	c = Counter(template)
	return c[max(c, key=c.get)] - c[min(c, key=c.get)]

def exercise1(template, arr):
	for i in range(10):
		pairs = get_pairs(template)
		template = generate_string(pairs, arr)
	return calculate_string(template)

# No need to generate the actual string => just calculate the pairs
def exercise2(template, rules):
	c_pairs_init = Counter(get_pairs(template))
	c_elements = Counter(template)
	for _ in range(40): 
		c_pairs_final = Counter()
		for pair in c_pairs_init.keys(): 
			insertion, old_count = rules[pair], c_pairs_init[pair] 
			c_pairs_final[pair[0] + insertion] += old_count 
			c_pairs_final[insertion + pair[-1]] += old_count 
			c_elements[insertion] += old_count 
		c_pairs_init = c_pairs_final 
	m = c_elements.most_common() 
	return m[0][1] - m[-1][1]

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
	template = arr[0]
	split = [i.split(" -> ") for i in arr[2:]]
	inputs = {i:j for i,j in split}

	result = exercise1(template, inputs.copy())
	print(result)
	result = exercise2(template, inputs.copy())
	print(result)
