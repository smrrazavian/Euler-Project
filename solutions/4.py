import time

def first_try():
    start_time = time.time()
    num = []

    for a in range(100, 1000):
        for b in range(a, 1000):
            s = str(a * b)
            if s == s[::-1]:
                num.append(a * b)

    end_time = time.time()
    print (max(num) , "The program running time is: " , end_time - start_time)


def second_try():
    start_time = time.time()
    max_num = 0
    for a in range(100, 1000):
        for b in range(a, 1000):
            if a * b < max_num:
                continue
            s = str(a * b)
            if s == s[::-1]:
                max_num = a * b
    end_time = time.time()
    print(max_num, "The program running time is: " , end_time - start_time)

if __name__ == '__main__':
    second_try()