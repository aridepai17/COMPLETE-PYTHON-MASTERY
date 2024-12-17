'''
Write a program that determines if a word is a palindrome.
'''

string = input('Enter a word: ')
string = string.lower()
reverse = string[::-1]
if string == reverse:
    print('The word is a palindrome.')
else:
    print('The word is not a palindrome.')