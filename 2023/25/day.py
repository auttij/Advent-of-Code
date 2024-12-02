import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
import networkx as nx

@timer
@print_result
def part1(input):
	G = nx.Graph()

	for line in input:
		label, conns = line.split(": ")
		conns = conns.split(" ")
		for conn in conns:
			G.add_edge(label, conn, capacity=1)

	start = "bzh"
	end = max(nx.shortest_path(G, start).items(), key=lambda x: len(x[1]))[0]

	val, partition = nx.minimum_cut(G, start, end)
	return len(partition[0]) * len(partition[1])


def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	part1(input)

if __name__ == "__main__":
	main(argv[1:])
