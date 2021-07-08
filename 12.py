from math import sqrt
import time

t = time.time()


def q(b):
    a = 0
    for i in range(1, int(sqrt(b))+1):
        if b % i == 0: a += 1
    if a * 2 > 500: return True


b = 0

for a in range(100000):
    b = a * (a+1)/2
    if q(b):
        print(b)
        break
print("solved in :", time.time() - t)

