
def frist_approach():
    num = [1, 2]
    total = 0
    for i in range(4000000):
        if i == num[-1] + num[-2]:
            num.append(i)

    for x in num:
        if x % 2 == 0:
            total += x

    print(total)


def second_approach():
    a, b = 1, 2
    total = 0
    
    while a <= 4000000:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    
    print(total)

if __name__ == '__main__':
    second_approach()
    


