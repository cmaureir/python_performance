import time
import functools


@functools.cache
def factorial1(n):
    return n * factorial1(n-1) if n else 1

@functools.lru_cache
def factorial2(n):
    return n * factorial2(n-1) if n else 1

N = 400

t_start = time.perf_counter_ns()
a = factorial1(N)
t_end = time.perf_counter_ns()
print(f"factorial1({N})", (t_end-t_start)/10**9)

t_start = time.perf_counter_ns()
b = factorial1(N)
t_end = time.perf_counter_ns()
print(f"factorial1({N})", (t_end-t_start)/10**9)


t_start = time.perf_counter_ns()
c = factorial2(N)
t_end = time.perf_counter_ns()
print(f"factorial2({N})", (t_end-t_start)/10**9)

t_start = time.perf_counter_ns()
d = factorial2(N)
t_end = time.perf_counter_ns()
print(f"factorial2({N})", (t_end-t_start)/10**9)
