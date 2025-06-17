import random
import string

def generate_password(length):
    # Define characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt user for password length
try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Password length must be a positive number.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
