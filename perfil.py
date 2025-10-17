import time
import random

def f(lst):
    t = 0
    for i in lst:
        for j in i:
            t += j
    return t

def g(lst):
    t = 0
    for i in lst:
        t += sum(i)
    return t


N = 5_000
l =  [[random.random() for i in range(N)] for _ in range(N)]

t_start = time.perf_counter_ns()
print(f(l))
print(f"Time with f: {(time.perf_counter_ns() - t_start)/10**9}")
t_start = time.perf_counter_ns()
print(g(l))
print(f"Time with g: {(time.perf_counter_ns() - t_start)/10**9}")
