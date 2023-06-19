from time import time

start = time()


def fib(n):
    a = 1
    b = 0
    while n > 1:
        a, b = a + b, a
        n = n - 1
    return a


for i in range(1, 10000):
    if len(str(fib(i))) == 1000:
        print(i)
        break

elapsed = (time() - start)
print("This code took: " + str(elapsed) + " seconds")

# --------------------------------------------------

start = time()

memo = {0: 0, 1: 1}


def fib(n):
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


for i in range(1, 10000):
    if len(str(fib(i))) == 1000:
        print(i)
        break

elapsed = (time() - start)
print("This code took: " + str(elapsed) + " seconds")