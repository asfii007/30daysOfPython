#Convert a list of mixed strings and numbers to a list of floats, ignoring invalid values.
a=["asfiya",3,19]
lst=[]
for i in a:
    try:
        lst.append(float(i))
    except ValueError:# skip items that cannot be converted to float
        pass 
    #except ValueError: catches that error and the pass does nothing, so the program continues to the next item instead of crashing.
    
print(lst)
