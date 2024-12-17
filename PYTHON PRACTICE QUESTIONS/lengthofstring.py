'''
Write a program that determines the length of a string without using
len() function.
'''

string = input('Enter a string: ')
length = 0
for char in string:
    length += 1
    
print(length)