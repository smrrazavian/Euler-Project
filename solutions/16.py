from time import time
from math import pow

start = time()

#n = int(input("Enter the power : "))
n = 1000
b = int(pow(2, n))
a = 0

while b > 0:
    a += b % 10
    b //= 10

print(a)

elapsed = (time() - start)
print("This code took: " + str(elapsed) + " seconds")