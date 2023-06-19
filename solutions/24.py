from time import time
from math import factorial

start = time()
a = factorial(10)
elapsed = (time() - start)
print("This code took: " + str(elapsed) + " seconds")