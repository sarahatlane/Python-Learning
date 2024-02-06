# creating a simple program that generates a random password based on the user's specifications. 
# We'll allow the user to specify the length of the password and whether it should include lowercase letters, uppercase letters, digits, and special characters.

import random
import string

def generate_password(length, use_lower=True, use_upper=True, use_digits=True, use_special=True):
    # Define character sets based on user specifications
    characters = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation


 # Generate password using random.choices() (Python 3.6+)
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password: "))
    use_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_lower, use_upper, use_digits, use_special)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()