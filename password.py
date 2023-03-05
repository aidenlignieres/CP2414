import hashlib
import random
import string
import secrets

def generate_password(min_length=8, max_length=20, include_uppercase=True, include_lowercase=True, include_numbers=True, include_symbols=True):
    """Generate a random password that meets the given criteria."""
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if len(characters) == 0:
        raise ValueError("At least one character type must be included")
    while True:
        password = ''.join(random.choice(characters) for i in range(random.randint(min_length, max_length)))
        if (include_uppercase and any(c.isupper() for c in password)
                and include_lowercase and any(c.islower() for c in password)
                and include_numbers and any(c.isdigit() for c in password)
                and include_symbols and any(c in string.punctuation for c in password)):
            return password

def create_password_hash(password):
    """Create a SHA-256 hash of the given password."""
    salt = secrets.token_hex(16)
    password_with_salt = password + salt
    hashed_password = hashlib.sha256(password_with_salt.encode()).hexdigest()
    return (salt, hashed_password)

def create_user(username, password):
    """Create a new user with the given username and hashed password."""
    salt, hashed_password = create_password_hash(password)
    with open('users.txt', 'a') as file:
        file.write(f"{username}:{salt}:{hashed_password}\n")

def verify_password(username, password):
    """Verify that the given username and password match a stored user."""
    with open('users.txt', 'r') as file:
        for line in file:
            fields = line.strip().split(':')
            if fields[0] == username:
                salt = fields[1]
                hashed_password = fields[2]
                password_with_salt = password + salt
                hashed_password_to_check = hashlib.sha256(password_with_salt.encode()).hexdigest()
                return hashed_password_to_check == hashed_password
    return False

def create_account():
    """Create a new account with a user-specified username and password."""
    print("Creating a new account...")
    username = input("Enter a username: ")
    while True:
        password = input("Enter a password (or leave blank to generate one): ")
        if password == '':
            password = generate_password()
            print(f"Generated password: {password}")
        elif password != '':
            if verify_password(username, password) == False:
                create_user(username, password)
                print(f"Account created for {username}")
                break
            else:
                print("This username is already taken. Please choose a different one.")


def login():
    """Log in with an existing account."""
    print("Logging in...")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if verify_password(username, password):
        print(f"Welcome, {username}!")
    else:
        print("Incorrect username or password. Please try again.")

def main():
    """Main function to run the program."""
    print("Welcome to the user login program!")
    while True:
        print("Choose an option:")
        print("1. Create a new account")
        print("2. Log in with an existing account")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
