num = []

for a in range(100, 1000):
    for b in range(a, 1000):
        s = str(a * b)
        if s == s[::-1]:
            num.append(a * b)

print(max(num))
