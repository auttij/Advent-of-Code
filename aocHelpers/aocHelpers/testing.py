from time import perf_counter
from typing import Callable, Iterable, Any


class TestCase:
    def __init__(self, name: str, input_data: Any, expected: Any):
        self.name = name
        self.input_data = input_data
        self.expected = expected


def run_tests(
    solver: Callable[[Any], Any], cases: Iterable[TestCase], *, show_time: bool = True
):
    """Runs solver(input) for each test case and prints colored results."""
    print("\n--- Running Tests ---")

    passed = 0
    total = 0

    for case in cases:
        total += 1
        print(f"\n[TEST] {case.name}")

        start = perf_counter()
        result = solver(case.input_data)
        end = perf_counter()

        if result == case.expected:
            print("  ✓ PASS")
            passed += 1
        else:
            print("  ✗ FAIL")
            print(f"    expected: {case.expected}")
            print(f"    got     : {result}")

        if show_time:
            print(f"    time: {(end - start) * 1000:.2f} ms")

    print(f"\n{passed}/{total} tests passed")
    return passed == total
