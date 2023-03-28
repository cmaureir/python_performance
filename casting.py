import time
from random import random
#from scalene import scalene_profiler
#from line_profiler import profile

N = 1_000

lst = [[random() for i in range(N)] for _ in range(N)]

#@profile
def a(super_list):
    s = 0
    for l in super_list:
        t = list(l)
        s += sum(t)
    return s

#@profile
def b(super_list):
    s = 0
    for l in super_list:
        s += sum(l)
    return s

#scalene_profiler.start()
#t1 = time.time()
o1 = a(lst)
#print("a:", time.time()-t1)
#
#t2 = time.time()
o2 = b(lst)
#print("b:", time.time()-t2)
#scalene_profiler.stop()
