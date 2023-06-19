from time import time
import math

start = time()

for a in range(1, 500):
    for b in range(a + 1, 500):
        c = 1000 - a - b
        if (a + b + c) > 1000:
            break
        if math.hypot(a, b) == c:
            print(f"{a * b * c}")
            elapsed = (time() - start)
            print(f"This code took: {elapsed:.6f} seconds")
            exit()