from time import time
from math import pow, floor, sqrt

start = time()

for a in range(1, 500):
    for b in range(a + 1, 500):
        c = 1000 - a - b
        if (pow(a, 2) + pow(b, 2) == pow(c, 2)) & (a + b + c == 1000):
            print(a * b * c)
            break

elapsed = (time() - start)
print("This code took: " + str(elapsed) + " seconds")
