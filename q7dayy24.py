#Given a tuple of integers, return the product of all elements without using loops.
def product_tuple(t):
    if len(t) == 0:       # base case: empty tuple
        return 1
    return t[0] * product_tuple(t[1:])  # multiply first element with product of the rest


numbers = (2,3,4)
print(product_tuple(numbers))
#t[1:] This is a slice of the tuple starting from the second element to the end.
'''product_tuple(t[1:])
This is a recursive call to the same function but with the smaller tuple (3, 4)
The function will again take the first element of (3, 4) (which is 3) and 
multiply it by product_tuple((4,)).'''

'''function starts returning values back up the chain:
product_tuple((4,)) → 4 * 1 = 4
product_tuple((3, 4)) → 3 * 4 = 12
product_tuple((2, 3, 4)) → 2 * 12 = 24'''