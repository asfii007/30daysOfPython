#Write a program that prints a formatted table of numbers from 1 to 10, their squares, and cubes.
print("number square cube")
for i in [1,2,3,4,5,6,7,8,9,10]:
    num=i
    sq=i*i
    cube=i**3#<6 part is used for alignment and width of the column
    print(f"{num:<6}  {sq:<6} {cube:<6}")
