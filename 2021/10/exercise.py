import sys
sys.path.insert(0,'..')
import helpers
from collections import deque

def get_unmatched_parenthesis(s: str) -> str:
	pair = {")": "(", "]": "[", "}": "{", ">": "<"}
	def rec(s: str, stack: list[str]):
		if len(s) == 0:
			if len(stack) > 0:
				return stack
			else:
				return []
		char = s[0]
		if char in ")]}>":
			if stack[0] != pair[char]:
				return [char]
			else:
				stack.pop(0)
				return rec(s[1:], stack)
		elif char in "([{<":
			return rec(s[1:], [s[0]] + stack)
	return rec(s, [])

def character_to_points(s: str) -> int:
	if s == ")":
		return 3
	elif s == "]":
		return 57
	elif s == "}":
		return 1197
	elif s == ">":
		return 25137

def create_completion_string(stack: list[str]) -> list[str]:
	pair = {"(": ")", "[": "]", "{":"}", "<":">" }
	def rec(input: list[str], out: list[str]):
		if len(input) == 0:
			return out
		char = input[0]
		return rec(input[1:], out + [pair[char]])
	return rec(stack, [])

def calculate_complete_string_score(stack: list[str]) -> int:
	points = {")": 1, "]": 2, "}": 3, ">": 4}
	def rec(stack: list[str], score: int) -> int:
		if len(stack) == 0:
			return score
		char = stack[0]
		return rec(stack[1:], score * 5 + points[char])
	return rec(stack, 0)

def is_incomplete(s: list[int]) -> bool:
	return len(s) >= 1 and s[0] in "([{<"

def exercise1(arr):
	parenthesis = map(get_unmatched_parenthesis, arr)
	corrupted = filter(lambda x: len(x) == 1, parenthesis)
	corrupted_chars = map(lambda x: x[0], corrupted)
	char_scores = map(character_to_points, corrupted_chars)
	return sum(char_scores)

def exercise2(arr):
	parenthesis = map(get_unmatched_parenthesis, arr)
	incomplete = filter(is_incomplete, parenthesis)
	completion_strings = map(lambda x: create_completion_string(x), incomplete)
	string_scores = map(calculate_complete_string_score, completion_strings)
	sorted_scores = sorted(string_scores)
	return sorted_scores[int(len(sorted_scores) / 2)]



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
