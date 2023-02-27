import random, string

SYMBOLES = "!@#$%^&*().?<>/"


def generate_password():
    a = ""
    while not is_valid_password(a):
        for i in range(random.randint(8, 20)):
            choice = random.randint(0, 3)
            if choice == 0:
                a += random.choice(string.ascii_letters)
            elif choice == 1:
                a += random.choice(SYMBOLES)
            elif choice == 2:
                a += str(random.randint(0, 10))
    return a


def is_valid_password(password):
    """Determine if the provided password is valid."""
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char in SYMBOLES:
            count_special += 1
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    if count_special == 0:
        return False

        # if we get here (without returning False), then the password must be valid
    return True


def main():
    for i in range(20):
        a = generate_password()
        print(a)
        print(len(a))


main()
