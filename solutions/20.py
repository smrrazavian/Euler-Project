from time import time
from math import factorial

start = time()
a = str(factorial(100))

b = sum(int(i) for i in a)

print(b)

elapsed = (time() - start)
print("This code took: " + str(elapsed) + " seconds")