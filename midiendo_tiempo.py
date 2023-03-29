import time


def f(lst, v):
    total = 0
    t1 = time.time()
    for i in lst:
        total += i ** v
    t2 = time.time()
    return total, t2-t1

def g(lst, v):
    total = 0
    t1 = time.perf_counter_ns()
    for i in lst:
        total += i ** v
    t2 = time.perf_counter_ns()
    return total, (t2-t1)/(10**9)

print("Using time.time()")
print(f([1], 1))
print(f([1,2], 1))
print(f(range(10), 2))
print(f(range(100), 3))
print(f(range(10_000), 2))

print("Using time.perf_counter_ns()")
print(g([1], 1))
print(g([1,2], 1))
print(g(range(10), 2))
print(g(range(100), 3))
print(g(range(10000), 2))
