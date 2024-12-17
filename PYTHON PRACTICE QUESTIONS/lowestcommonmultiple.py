'''
Write a program that returns the least common multiple of two numbers.
'''

def lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    lcm = (a * b) // gcd(a, b)
    return lcm

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
result = lcm(num1, num2)