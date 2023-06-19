import time

t = time.time()
total_sum = 2
N = 2000000
sieve = [True] * N
sieve[0] = sieve[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, N, i):
            sieve[j] = False

for i in range(3, N):
    if sieve[i]:
        total_sum += i

print(total_sum)
print("Solved in : ", time.time() - t)