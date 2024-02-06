# defining a dictionary called credentials where the keys are usernames and the values are passwords.
# defining a function login() that prompts the user to enter their username and password using the input() function.
# Inside the login() function, we check if the entered username exists in the credentials dictionary and if the entered password matches the password associated with that username.
# If the username and password are correct, we print a success message. Otherwise, we print an error message.

# Define a dictionary to store usernames and passwords
credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

def login():
    # Ask the user for their username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

# Check if the username exists and the password is correct
    if username in credentials and credentials[username] == password:
        print("Login successful! Welcome, " + username + "!")
    else:
        print("Invalid username or password. Please try again.")

# Call the login function to start the login process
login()