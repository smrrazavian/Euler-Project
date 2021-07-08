import time
start_time = time.time()
x = 2
a = 600851475143

while x < (a / x):
    if a % x == 0 :
        a = a/x
    else :
        x += 1

end_time = time.time()

print (a , "The progra, runnig thime is : " , end_time - start_time)
