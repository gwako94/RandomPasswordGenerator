import string
import random 

special_characters = '#$%&!@*'
#This will generate a string consist of all required characters
passwrd = string.ascii_letters+string.digits+special_characters
length = int(input("Enter the length of the password: "))


def generate_password():
    password=''
    for c in range(length):
        password += random.choice(passwrd) # Choice() function returns a random element from a iterable element.
    return password
    
    
print(generate_password())