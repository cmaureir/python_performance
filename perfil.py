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
l =  [[random.random() for i in range(N) for _ in range(N)]]

print(f(l))
print(g(l))


