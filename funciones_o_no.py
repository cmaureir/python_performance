import time

def get_time(f):

    def w(*args, **kwargs):
        t1 = time.perf_counter_ns()
        r = f(*args, **kwargs)
        return r, (time.perf_counter_ns() - t1) / 10**9

    return w

def calculo(x, y):
    return 10**x + y

@get_time
def f():
    base = 2
    r = 0
    for i in range(1_000_000):
        r += calculo(base, i)
    return r

@get_time
def g():
    base = 2
    r = 0
    for i in range(1_000_000):
        r += 10**base + i
    return r


a = f()[1]
b = g()[1]

print("función  ", a)
print("operación", b)
print("fraction ", b*100/a)
