def dif(n):
    s = 0
    for i in range(1 , n+1):
        s += i**2

    m = ((n * (n+1))/2) ** 2

    print(abs(s - m))

dif(100)
