#zip
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(list(zip(a, b)))

#map
nums = [1, 2, 3, 4]

print(list(map(lambda x: x*x, nums)))
# [1, 4, 9, 16]
"""map(function, iterable)
 Here function = lambda x: x*x  
 iterable = nums
 1 → 1*1 = 1
 2 → 2*2 = 4
 3 → 3*3 = 9
 4 → 4*4 = 16 """
nums = [1, 2, 3, 4, 5, 6]

#filter
#keep only even numbers
print(list(filter(lambda x: x % 2 == 0, nums)))
# [2, 4, 6]
