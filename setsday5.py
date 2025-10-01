#set1
colors={"blue","green","red","yellow","green"}
print(colors) #no duplicates
#set methods
colors.add("white")
print(colors)
colors.remove("blue")
print(colors)
print("red" in colors)

#set2
multi={"apple", "banana", "cherry", False, True, 0}
print(multi)

# set3
A={4,8,5,89,67,3,78,44}
B={56,89,76,3,24,78,6,}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B)) #Elements that are in A but not in B.
print(A.symmetric_difference(B)) #Elements that are in either set, but NOT in both.