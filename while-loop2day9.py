#Write a program that uses a while loop to count down from 10 to 1, then prints "Blast off!".
import time # lets us use the sleep() function
a=10
while a>=1:
    print(a)
    a-=1
    time.sleep(1) ## wait for 1 second
print("Blast off!")