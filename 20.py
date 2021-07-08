from time import time
from math import factorial

start = time()
a = str(factorial(100))

b = 0
for i in a:
    b = int(i) + b

print(b)

elapsed = (time() - start)
print("This code took: " + str(elapsed) + " seconds")
