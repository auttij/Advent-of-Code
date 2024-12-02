import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

class Monkey:
	def __init__(self, items, operation, testDivider, target1, target2, r2=False):
		self.items = [int(i) for i in items]
		self.operand1 = operation.split(' ')[0]
		self.operator = operation.split(' ')[1]
		self.operand2 = operation.split(' ')[2]
		self.testDividier = int(testDivider)
		self.target1 = int(target1)
		self.target2 = int(target2)
		self.inspections = 0
		self.r2 = r2

	def getWorry(self, item):
		s = ''
		if self.operand1 == 'old':
			s += str(item)
		else:
			s += self.operand1
		s += self.operator
		if self.operand2 == 'old':
			s += str(item)
		else:
			s += self.operand2
		
		if self.r2:
			return eval(s) % self.testDividier
		return eval(s) // 3

	def getTarget(self, item):
		if item % self.testDividier == 0:
			return self.target1
		return self.target2

	def round(self):
		newWorries = list(map(self.getWorry, self.items))
		targets = list(map(self.getTarget, newWorries))
		self.items = []
		self.inspections += len(newWorries)
		return list(zip(newWorries, targets))

	def addItem(self, item):
		self.items.append(item)

	def setModulo(self, modulo):
		self.testDividier = modulo

	def __repr__(self) -> str:
		return str(self.items)

@timer
@print_result
def exercise1(monkeys):
	inspections = [0 for _ in range(len(monkeys))]
	for _ in range(20):
		for i, m in enumerate(monkeys):
			round = m.round()
			inspections[i] += len(round)
			for item, target in round:
				monkeys[target].addItem(item)
		# print(monkeys)

	o = sorted(inspections, reverse=True)[:2]
	return o[0] * o[1]

@timer
@print_result
def exercise2(monkeys):
	inspections = [0 for _ in range(len(monkeys))]

	for r in range(10000):
		if r % 100 == 0:
			print(r, end='\r')

		for i, m in enumerate(monkeys):
			round = m.round()
			inspections[i] += len(round)
			for item, target in round:
				monkeys[target].addItem(item)
		# print(monkeys)

	o = sorted(inspections, reverse=True)[:2]
	return o[0] * o[1]

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	monkeys = []
	
	supermodulo = 1
	for line in arr:
		a, b = line.split('|')
		items = eval(a)
		others = b.split(',')
		supermodulo *= int(others[1].strip())
		print(others)
		monkeys.append(Monkey(items, *others))
	for m in monkeys:
		m.setModulo = supermodulo

	exercise1(monkeys.copy())
	exercise2(monkeys.copy())

if __name__ == "__main__":
	main(argv[1:])
