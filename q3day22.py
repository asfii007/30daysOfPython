#Count the frequency of each word in a sentence (case-insensitive).
sent="Python is fun and Python makes learning programming fun and easy"
sent=sent.lower()
words= sent.split()
#['python', 'is', 'fun', 'and', 'python', 'makes', 'learning', 'programming', 'fun', 'and', 'easy']
fre={}
for i in words:
    if i in fre:
        fre[i] +=1
    else:
        fre[i] =1
    #Checks if the word is already a key in the dictionary.
    #If yes, increment its count by 1 (fre[i] += 1).
    #If no, add it as a new key with count 1 (fre[i] = 1).
print(fre)   
