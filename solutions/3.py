import time
start_time = time.time()
x = 2
a = 600851475143

while x < (sqrt_a := int(a ** 0.5)):
    if a % x == 0 :
        a = a//x
    else :
        x += 1

end_time = time.time()

print (a , "The program running time is: " , end_time - start_time)