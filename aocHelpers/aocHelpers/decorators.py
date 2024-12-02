import logging
from time import perf_counter


def timer(func):
	'''Decorator that logs the execution time'''
	
	def wrap(*args, **kwargs):
		start = perf_counter()
		result = func(*args, **kwargs)
		end = perf_counter()

		logging.info(f"{(end - start )* 1000} ms")
		
		return result
	return wrap

def print_result(func):
	'''Decorator that prints the result of the executed function'''
	def wrap(*args, **kwargs):
		result = func(*args, **kwargs)
		logging.info(f"{func.__name__}:")
		logging.info(f"{result = }")
		return result
	return wrap
