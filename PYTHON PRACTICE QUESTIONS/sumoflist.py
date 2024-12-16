'''
Write a program to find the sum of elements in a list.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum(numbers)
print("The sum of elements in the list is", total)

# Without using the sum() function:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for number in numbers:
    total += number

print("The sum of elements in the list is", total)

