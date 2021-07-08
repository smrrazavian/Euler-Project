import time

t = time.time()
sum = 2


def is_prime(n):
    avval = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            avval = False
            break
    return avval


for i in range(3, 2000000):
    if is_prime(i):
        sum = sum + i
print(sum)
print("Solved in : ", time.time() - t)
