import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.5f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num):
    for _ in range(num):
        sum([i**2 for i in range(10000)])

waste_some_time(1)
waste_some_time(3)