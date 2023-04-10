import time


def get_time(f):
    def w(*args, **kwargs):
        t1 = time.perf_counter_ns()
        r = f(*args, **kwargs)
        return r, (time.perf_counter_ns() - t1) / 10**9

    return w


def is_leap(year):
    if (year % 400 == 0) and (year % 100 == 0) or (year % 4 == 0) and (year % 100 != 0):
        return True
    return False


@get_time
def f(years):
    leaps = []
    for year in years:
        if is_leap(year):
            leaps.append(year)
    return leaps


@get_time
def g(years):
    return [year for year in years if is_leap(year)]


ys = list(range(10_000_000))

a = f(ys)[1]
b = g(ys)[1]
print("loop         ", a)
print("comprehension", b)
print("fraction     ", b * 100 / a)
