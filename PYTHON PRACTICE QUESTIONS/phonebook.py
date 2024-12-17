'''
Write a program that creates a phonebook dictionary with names as keys,
and phone numbers as values. Allow the user to look up a number by name.
'''

phonebook = {
    "Alice": "703-493-1834",
    "Bob": "857-384-1234",
    "Elizabeth": "484-584-2923",
    "Kareem": "938-489-1234",
    "Simone": "968-345-2345"
}

name = input("Enter a name: ")
print("Phone number: ", phonebook.get(name, "Name not found"))