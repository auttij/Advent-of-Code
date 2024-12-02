import sys
sys.path.insert(0,'..')
import helpers

"""
Helper class to keep track of a single bingo board
and to determine if it has won yet or no
"""
class Bingo():
	def __init__(self, board):
		self.board = board
		self.rows = len(self.board)
		self.cols = len(self.board[0])
		self.result = [[0 for i in range(self.cols)] for j in range(self.rows)]

	def unmarked(self):
		out = []
		for i, row in enumerate(self.result):
			for j, num in enumerate(row):
				if num == 0:
					out.append(self.board[i][j])
		return out

	def check_win(self):
		row_results = [sum(i) for i in self.result]
		row_win = any([i == self.rows for i in row_results])

		result_trans = helpers.transpose(self.result)
		col_results = [sum(i) for i in result_trans]
		col_win = any([i == self.cols for i in col_results])
		if row_win or col_win:
			return self.unmarked()
		else:
			return 0

	def place_number(self, num):
		for i, row in enumerate(self.board):
			for j, elem in enumerate(row):
				if elem == num:
					self.result[i][j] = 1

"""Helper functions to create multiple Bingo-objects from input"""
def create_bingos(arr):
	numbers = arr[0].split(",")
	bingos = []
	new_sheet = []
	for i, row in enumerate(arr[2:]):
		if row == "":
			nb = Bingo(new_sheet)
			bingos.append(nb)
			new_sheet = []
		else:
			new_sheet.append(row.split())
	nb = Bingo(new_sheet)
	bingos.append(nb)
	return numbers, bingos

"""
Figure which bingo sheet wins first
return sum of unmarked numbers on that sheet, multiplied by winning number
"""
def exercise1(arr):
	numbers, bingos = create_bingos(arr)
	
	for num in numbers:
		for b in bingos:
			b.place_number(num)
			res = b.check_win()
			if res != 0:
				return int(num) * sum([int(i) for i in res])

"""
Figure which bingo sheet wins last
return sum of unmarked numbers on that sheet, multiplied by winning number
"""
def exercise2(arr):
	numbers, bingos = create_bingos(arr)
	wins = [0 for i in range(len(bingos))]

	for num in numbers:
		for bi, b in enumerate(bingos):
			if wins[bi] == 0:
				b.place_number(num)
				res = b.check_win()
				
				if res != 0:
					if wins.count(0) > 1:
						wins[bi] = int(num)
					else:
						return int(num) * sum([int(i) for i in res])

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
