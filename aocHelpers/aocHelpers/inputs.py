import logging
import re

def read_to_str(filepath):
	logging.info(f"reading file: {filepath}")
	with open(filepath) as fp:
		return "".join(fp.readlines())

def read_to_str_arr(filepath):
	logging.info(f"reading file: {filepath}")
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def read_to_2d_str_arr(filepath):
	logging.info(f"reading file: {filepath}")
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		subArr = []
		for line in lines:
			val = line.strip()
			if len(val) > 0:
				subArr.append(val)
			else:
				arr.append(subArr)
				subArr = []
	return arr

def read_to_str_pair_arr(filepath):
	logging.info(f"reading file: {filepath}")
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.split())
	return arr

def read_to_int_arr(filepath):
	logging.info(f"reading file: {filepath}")
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(int(line.strip()))
	return arr

def read_to_2d_int_arr(filepath):
	logging.info(f"reading file: {filepath}")
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		subArr = []
		for line in lines:
			val = line.strip()
			if val:
				subArr.append(int(val))
			else:
				arr.append(subArr)
				subArr = []
	return arr

def read_to_int_tuple_arr(filepath):
	logging.info(f"reading file: {filepath}")
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(tuple(map(int, re.findall(r'\d+', line))))
	return arr