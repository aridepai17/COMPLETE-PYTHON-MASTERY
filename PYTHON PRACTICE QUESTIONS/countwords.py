'''
Write a program that counts the occurrences of each word 
in a given string and stores the results in a dictionary.
'''

text = 'cant seem to forget the pain you seem to give the pain you seem to give my friend'

words = text.split()
wordcount = {}

for word in words:
    if word in wordcount:
        wordcount[ word ] += 1
    else:
        wordcount[ word ] = 1
        
print(wordcount)