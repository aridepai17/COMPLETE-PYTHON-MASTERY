'''
Write a function to compute the greatest common divisor of two numbers.
'''

def gcd( a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
result = gcd(num1, num2)
print(result)