from numpy import lcm, arange
import time

t = time.time()

list = arange(11,20)

x = lcm.reduce(list)
print(x)
print(time.time() - t)
