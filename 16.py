from time import time
from math import pow

start = time()

#n = int(input("Enter the power : "))
n = 1000
b = str(int(pow(2, n)))
a = 0

for i in b:
    a = int(i) + a

print(a)

elapsed = (time() - start)
print("This code took: " + str(elapsed) + " seconds")
