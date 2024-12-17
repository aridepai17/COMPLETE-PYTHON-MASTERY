'''
Write a program to check whether a number is prime or not.
'''

def prime():
    if num <= 1:
        return False
    for  i in range(2, num):
        if num % i == 0:
            return False
        return True
    
num = int(input('Enter a number: '))
result = prime()
if result:
    print(f'{num} is a prime number')