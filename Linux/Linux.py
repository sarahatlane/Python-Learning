import random
import string
import argparse

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument("length", type=int, help="Length of the password")
    args = parser.parse_args()
    
    if args.length <= 0:
        print("Error: Length must be a positive integer.")
    else:
        password = generate_password(args.length)
        print("Generated Password:", password)
