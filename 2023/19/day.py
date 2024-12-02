import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def part1(workflows, parts):
	out = 0
	for part in parts:
		print(f'{part = }')
		wk = "in"
		finished = False
		accepted = False
		while not finished:
			w = workflows[wk]
			print(f'{wk = }', w)
			for rule in w:
				print(f'{rule = }')
				if not 'var' in rule:
					res = rule['res']
					if res == 'A':
						accepted = True
					if res == 'A' or res == 'R':
						finished = True 
					if res != 'R':
						wk = res
					break

				else:
					ehto = f"{part[rule['var']]}{rule['comp']}{rule['val']}"
					if eval(ehto):
						res = rule['res']
						if res == 'A':
							accepted = True
						if res == 'A' or res == 'R':
							finished = True 
						if res != 'R':
							wk = res
						break
		if accepted:
			out += part['x'] + part['m'] + part['a'] + part['s']

			print(w)

	return out

def both(ch, gt, val, ranges):
	ch = 'xmas'.index(ch)
	ranges2 = []
	for rng in ranges:
		rng = list(rng)
		lo, hi = rng[ch]
		if gt:
			lo = max(lo, val + 1)
		else:
			hi = min(hi, val - 1)
		if lo > hi:
			continue
		rng[ch] = (lo, hi)
		ranges2.append(tuple(rng))
	return ranges2

wfs = {}
def outer(w):
	return f(wfs[w])

def f(w):
	r = w[0]
	res = r['res']
	if 'var' not in r:
		if res == 'R':
			return []
		if res == 'A':
			return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
		return outer(r['res'])

	gt = '>' == r['comp']
	ch = r['var']
	val = r['val']
	val_inverted = val + 1 if gt else val - 1


	if_cond_is_true = both(ch, gt, val, f([{'res': res}]))
	if_cond_is_false = both(ch, not gt, val_inverted, f(w[1:]))
	return if_cond_is_true + if_cond_is_false


@timer
@print_result
def part2(workflows):
	out = 0
	for rng in outer('in'):
		v = 1
		for lo, hi in rng:
			v *= hi - lo + 1
		out += v
	return out


def parse(input):
	a, b = input.split("\n\n")
	workflows = {}
	for line in a.split("\n"):
		key, end = line.split("{")
		rules = end[:-1].split(",")
		r_a = []
		for rule in rules:
			if len(rule) == 1 or ":" not in rule:
				r_a.append({'res': rule})
				continue

			r_a.append({
				'var': rule[0],
				'comp': rule[1],
				'val': int(rule.split(":")[0][2:]),
				'res': rule.split(":")[1],
			})
		workflows[key] = r_a
		wfs[key] = r_a
	
	parts = []
	for line in b.split("\n"):
		vars = line[1:-1].split(",")
		splt = [x.split("=") for x in vars]
		obj = { key: int(val) for key, val in splt}
		parts.append(obj)

	return workflows, parts

def main(args=None):
	data = init(path.dirname(__file__), inputs.read_to_str, args)
	workflows, parts = parse(data)
	# part1(workflows, parts)
	part2(workflows)
if __name__ == "__main__":
	main(argv[1:])
