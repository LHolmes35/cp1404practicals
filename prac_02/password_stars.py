
MINIMUM_LENGTH = 8


def main():
    user_password = get_password()
    print_password(user_password)


def get_password():
    """Determine if password is valid"""
    user_password = input("Please input password: ")
    while len(user_password) < MINIMUM_LENGTH:
        print("Invalid password")
        user_password = input("Please input password: ")
    return user_password


def print_password(user_password):
    """Print password as stars"""
    for i in range(len(user_password)):
        print("*", end='')
    print()


main()
