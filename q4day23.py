#Check if a given string is a pangram (contains all letters of the alphabet at least once).
import string
str="Focus on the journey not the destination "
str=str.lower()
letters=set("Focus on the journey not the destination" )
#{'y', 'r', 's', 'n', 'u', 'd', 'a', ' ', 'h', 'F', 'j', 't', 'o', 'c', 'e', 'i'}
alphabet=set(string.ascii_lowercase) 
#string.ascii_lowercase is just a predefined string
#get all lowercase letters (alphabet)
#{'v', 'g', 't', 'm', 'd', 'q', 'y', 'u', 'z', 'o', 'n', 'e', 'w', 's', 'k', 'c', 'a', 'l', 'h', 'b', 'x', 'r', 'p', 'f', 'i', 'j'}
if alphabet.issubset(letters): #A.issubset(B) checks if all elements of set A are inside set B.
# check if alphabet ⊆ letters
    print("it is a pangram")
else:
    print ("it is not a pangram")