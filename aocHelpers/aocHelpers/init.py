import sys
import argparse
import logging
from os import path

def get_arg_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('input', type=int, default=1, choices=range(1,5), help='Used input file number')
	parser.add_argument('--logging', '-l', type = str.lower, default="info", choices=["debug", "info", "warn", "error", "critical"])
	return parser

def init_logging(log_path, log_key = "info"):
	log_file = path.join(log_path, "log.log")
	log_level_map = { 
		"debug": logging.DEBUG, 
		"info": logging.INFO,
		"warn": logging.WARN,
		"error": logging.ERROR,
		"critical": logging.CRITICAL}

	log_level = log_level_map[log_key]

	logging.basicConfig(
		level=log_level, 
		format="[%(levelname)s] %(message)s",
		handlers=[
			logging.FileHandler(log_file),
			logging.StreamHandler(sys.stdout)
	]
	)
	logging.info(f"writing logs to {log_file = } with {log_key = }")

def init(__dir__, input_func, args=None):
	# Create arg parser
	parser = get_arg_parser()

	# parse args
	pargs = parser.parse_args(args)

	# init logging
	init_logging(__dir__, pargs.logging)

	# determine input file
	filename = path.join(__dir__, f"input{pargs.input}.txt")
	logging.info(f"using input {filename = }")
	logging.info(f"reading input using {input_func.__name__}")
	return input_func(filename)
