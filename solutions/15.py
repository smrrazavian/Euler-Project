import time
from math import factorial, pow

start = time.time()

n = 20

b = factorial(2 * n) / pow(factorial(n), 2)

print(b)
elapsed = (time.time() - start)
print(f"This code took: {elapsed} seconds")