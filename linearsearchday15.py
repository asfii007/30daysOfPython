#linear search
def linear(lst,key):
    for i in range(len(lst)):
        if lst[i]==key:
            return i #found key
    return "key not found"
list=[9,7,5,4,99]
print(linear(list,89))
print(linear(list,7))
