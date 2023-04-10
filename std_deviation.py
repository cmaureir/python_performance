import time
import random
from numpy import std, array

def get_time(f):

    def w(*args, **kwargs):
        t1 = time.perf_counter_ns()
        r = f(*args, **kwargs)
        return r, (time.perf_counter_ns() - t1) / 10**9

    return w

@get_time
def std1(lst):
    s = 0
    for i in lst:
        mean = sum(lst) / len(lst)
        s += (i - mean) ** 2
    return (s/len(lst)) ** 0.5

@get_time
def std2(lst):
    s = 0
    len_lst = len(lst)
    for i in lst:
        mean = sum(lst) / len_lst
        s += (i - mean) ** 2
    return (s/len_lst) ** 0.5

@get_time
def std3(lst):
    s = 0
    mean = sum(lst) / len(lst)
    for i in lst:
        s += (i - mean) ** 2
    return (s/len(lst)) ** 0.5

@get_time
def std4(lst):
    s = 0
    len_lst = len(lst)
    mean = sum(lst) / len_lst
    for i in lst:
        s += (i - mean) ** 2
    return (s / len_lst) ** 0.5

@get_time
def std5(lst):
    return std(lst)

@get_time
def std6(lst):
    return std(array(lst))

lst = [random.random() for _ in range(50_000)]
lst_a = array(lst)

print("base                ",std1(lst))
print("len                 ",std2(lst))
print("mean                ",std3(lst))
print("len mean            ",std4(lst))
print("numpy + list        ",std5(lst))
print("numpy + array       ",std5(lst_a))
print("numpy + list  + cast",std6(lst))
print("numpy + array + cast",std6(lst_a))
