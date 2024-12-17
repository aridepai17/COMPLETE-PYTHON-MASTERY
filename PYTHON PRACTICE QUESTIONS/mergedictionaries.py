'''
Write a program that merges two dictionaries.
'''

dict1 = { 'a': 1, 'b': 2, 'c': 3 }
dict2 = { 'd': 4, 'e': 5, 'f': 6 }
mergeddict = { **dict1, **dict2 }
print(mergeddict)