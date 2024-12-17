'''
Write a program to generate the Fibonacci sequence.
'''

def fibonacci(n):
    if n <= 0:
        return 'Invalid input'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
    return b

number = int(input('Enter a number: '))
result = fibonacci(number)
print(result)
    