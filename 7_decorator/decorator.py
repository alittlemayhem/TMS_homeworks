import time


def check_runtime(fibonacci):
    def time_for_fib():
        start_time = time.perf_counter_ns()
        result = fibonacci()
        end_time = time.perf_counter_ns()

        return result, end_time - start_time

    return time_for_fib


def recursive_fib(n: int) -> int:
    return 1 if n <= 2 else recursive_fib(n - 1) + recursive_fib(n - 2)

def dynamic_fib(n: int, memo: dict = {}) -> int:
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = dynamic_fib(n - 1, memo) + dynamic_fib(n - 2, memo)
    return memo[n]


@check_runtime
def recursive_runner():
    return recursive_fib(5)


@check_runtime
def dynamic_runner():
    return dynamic_fib(5)


recursive_result = recursive_runner()
dynamic_result = dynamic_runner()
print(f"Dynamic {dynamic_result} seems faster than recursive {recursive_result}")