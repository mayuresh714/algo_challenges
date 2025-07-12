import time
from code import optimise_multiplication

import multiprocessing

def worker(a, b, result_queue):
    try:
        from code import optimise_multiplication
        result = optimise_multiplication(a, b)
        result_queue.put((result, None))
    except Exception as e:
        result_queue.put((None, e))

def run_test(a, b, expected, idx):
    start = time.time()
    result_queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(a, b, result_queue))
    p.start()
    p.join(timeout=4.0)
    duration = time.time() - start

    if p.is_alive():
        p.terminate()
        p.join()
        print(f"Test {idx}: FAILURE (Timeout/Infinite Loop > 4s) | Input: ({a}, {b}) | Expected: {expected} | Got: <No Result> | Time: {duration:.2f}s")
        return False

    if not result_queue.empty():
        result, exception = result_queue.get()
        if exception is not None:
            print(f"Test {idx}: FAILURE (Exception) | Input: ({a}, {b}) | Exception: {exception}")
            return False
        if result != expected:
            print(f"Test {idx}: FAILURE | Input: ({a}, {b}) | Expected: {expected} | Got: {result}")
            return False
        print(f"Test {idx}: SUCCESS | Input: ({a}, {b}) | Output: {result} | Time: {duration:.2f}s")
        return True
    else:
        print(f"Test {idx}: FAILURE (No Result) | Input: ({a}, {b}) | Expected: {expected} | Got: <No Result>")
        return False

test_cases = [
    # Corner cases
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
    (0, 999999, 0),
    (999999, 0, 0),
    (1, 999999, 999999),
    (999999, 1, 999999),
    (2, 2, 4),
    (3, 4, 12),
    (7, 1, 7),
    (1, 7, 7),
    (123, 456, 56088),
    (999, 999, 998001),
    (100000, 100000, 10000000000),
    (10**6, 10**6, 10**12),
    (10**10, 1, 10**10),
    (1, 10**10, 10**10),
    (10**5, 10**5, 10**10),
    (10**8, 10**8, 10**16),
    (10**12, 10**12, 10**24),
    (10**15, 10**15, 10**30),
    (10**18, 1, 10**18),
    (1, 10**18, 10**18),
    (10**20, 10**20, 10**40),
    (10**100, 1, 10**100),
    (1, 10**100, 10**100),
    (10**100, 10**100, 10**200),
    (10**200, 10**200, 10**400),
    (10**300, 10**300, 10**600),
    (10**500, 10**500, 10**1000),
    (10**1000, 1, 10**1000),
    (1, 10**1000, 10**1000),
    (10**1000, 10**1000, 10**2000),
    (123456789, 987654321, 121932631112635269),
    (999999999, 999999999, 999999998000000001),
    (10**50, 10**50, 10**100),
    (10**500, 10**499, 10**999),
    (10**999, 10**999, 10**1998),
    (10**1000, 10**999, 10**1999),
    (10**1000, 10**1000-1, 10**2000-10**1000)
]

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    success_count = 0
    for idx, (a, b, expected) in enumerate(test_cases, 1):
        if run_test(a, b, expected, idx):
            success_count += 1

    if success_count == len(test_cases):
        print("\nAll test cases passed successfully! 🎉")
    else:
        print(f"\n{success_count}/{len(test_cases)} test cases passed.")
