import time

t = time.time()
solution_found = False
num = 2520


def is_composite(number):
    for i in range(11,20):
        if number % i != 0:
            return False
    return True


while solution_found == False:
    if is_composite(num):
        solution_found = True
        print(num)
    num += 2520
print(time.time() - t)
