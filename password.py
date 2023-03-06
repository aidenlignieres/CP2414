import hashlib
import random
import string
import secrets


def generate_password(min_length=8, max_length=20, include_uppercase=True, include_lowercase=True, include_numbers=True,
                      include_symbols=True):
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


def create_user(username, password):
    """Create a new user with the given username and hashed password."""
    salt = secrets.token_hex(16)
    password_with_salt = password + salt
    hashed_password = hashlib.sha256(password_with_salt.encode()).hexdigest()
    with open('users.txt', 'a') as file:
        file.write(f"{username}:{salt}:{hashed_password}\n")


def verify_password(password, salt, hashed_password):
    """Verify that the given password matches the given salt and hashed password."""
    password_with_salt = password + salt
    hashed_password_to_check = hashlib.sha256(password_with_salt.encode()).hexdigest()
    return hashed_password_to_check == hashed_password


def main():
    """Main function to run the program."""
    print("Login or Create User")

    print("Welcome to the user creation program!")
    print("Please enter a username and password to create a new user.")
    username = input("Username: ")

    generated_password = generate_password(include_uppercase=True, include_lowercase=True, include_numbers=True,
                                           include_symbols=True)
    print("Generated Password:", generated_password)

    while True:
        user_password = input("Password (press enter to use the generated password): ")
        if not user_password:
            user_password = generated_password
            break
        if (len(user_password) < 8 or len(user_password) > 20 or
                not any(c.isupper() for c in user_password) or
                not any(c.islower() for c in user_password) or
                not any(c.isdigit() for c in user_password) or
                not any(c in string.punctuation for c in user_password)):
            print(
                "Password must be 8-20 characters and contain at least one uppercase letter, one lowercase letter, one number, and one symbol.")
        else:
            break

    create_user(username, user_password)
    print(f"User '{username}' has been created with the password '{user_password}'.")


def caesar_cipher(password):
    step = int(input("Step: "))
    temp = ""
    for i in password:
        j = ord(i)
        k = (j + step) % 127
        if 32 < k < 127:
            temp += chr(k)
        else:
            temp += chr(k + 32)
    print(temp)

if __name__ == '__main__':
    main()
