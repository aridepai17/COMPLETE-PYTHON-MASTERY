'''
Write a program that checks if a number is even or odd.
'''

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is odd.")
    