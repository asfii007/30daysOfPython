#Binarysearch
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2   # middle index
        if lst[mid] == target:
            return mid            # found
        elif lst[mid] < target:
            low = mid + 1         # search right half
        else:
            high = mid - 1        # search left half
    
    return -1   # not found
data=[3,7,9,67,89]
print(binary_search(data,79))
print(binary_search(data,9))