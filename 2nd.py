num = [1, 2]
total = 0
for i in range(4000000):
    if i == num[-1] + num[-2]:
        num.append(i)

for x in num:
    if x % 2 == 0:
        total += x

print(total)
