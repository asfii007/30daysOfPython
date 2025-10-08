#Given two lists, return a list of all elements that appear in both lists without duplicates.
list1=[1,8,9,67,56,45,9]
list2=[9,67,5,3,89,20,45]
common=[]
for i in list1:
    if i in list2 and i not in common: #This checks if the element i exists anywhere inside list2
         #avoids duplication
         common.append(i)
print(common)