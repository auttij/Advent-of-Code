import logging
import copy
from time import perf_counter
from functools import wraps
from functools import lru_cache


def timer_print(func):
    """Decorator that prints execution time in ms."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"[TIMER] {func.__name__}: {(end - start)*1000:.3f} ms")
        return result

    return wrapper


def timer(func):
    """Decorator that logs execution time."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        logging.info(f"[TIMER] {func.__name__}: {(end - start)*1000:.3f} ms")
        return result

    return wrapper


def print_result(func):
    """Decorator that logs/prints the result of the function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"[RESULT] {func.__name__}: {result}")
        return result

    return wrapper


def aoc_part(func):
    """Decorator that prints result + execution time."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        import time

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}: {result}   [{(end-start)*1000:.3f} ms]")
        return result

    return wrapper


def check_no_mutation(func):
    """Warn if input argument is mutated during function execution."""

    @wraps(func)
    def wrapper(data, *args, **kwargs):
        before = copy.deepcopy(data)
        result = func(data, *args, **kwargs)
        if data != before:
            logging.warning(f"[WARNING] {func.__name__} mutated its input!")
        return result

    return wrapper


def benchmark(n=10):
    """Run function multiple times and print average runtime."""

    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total = 0
            result = None
            for _ in range(n):
                start = perf_counter()
                result = func(*args, **kwargs)
                end = perf_counter()
                total += end - start
            avg = (total / n) * 1000
            print(f"[BENCH] {func.__name__}: {avg:.3f} ms (avg over {n} runs)")
            return result

        return wrapper

    return deco


def cached(func):
    return lru_cache(None)(func)
