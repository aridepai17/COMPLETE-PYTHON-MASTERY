'''
Write a program to check whether two strings are anagrams of each other.
Anagrams -> Two strings are anagrams of each other if they 
contain the same characters.
'''

string1 = input('Enter the first string: ')
string2 = input('Enter the second string: ')

if sorted(string1) == sorted(string2):
    print('The strings are anagrams of each other.')
else:
    print('The strings are not anagrams of each other.')