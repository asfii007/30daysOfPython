#Ask the user to keep entering numbers, and add them together. Stop when the user enters 0, then print the sum.
total=0
i=1
while i>0:
    num=int(input("enter a no "))
    if num==0:
      break
    total=total+num
print(total)

#another version
'''total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print(total)
'''
#while True: instead of i = 1 and while i > 0 because True is a direct way to make an infinite loop
#  — it makes the code shorter and clearer.
