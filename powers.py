import time

def get_time(f):

    def w(*args, **kwargs):
        t1 = time.perf_counter_ns()
        r = f(*args, **kwargs)
        return r, (time.perf_counter_ns() - t1) / 10**9

    return w

N = 100_000

@get_time
def f():
  r = []
  for i in range(N):
    if i % 2 == 0:
        r.append(i**3)
  return r

@get_time
def g():
  return [i**3 for i in range(N) if i%2 == 0]


a = f()[1]
b = g()[1]
print("loop         ", a)
print("comprehension", b)
print("fraction     ", b*100/a)
