"""
Emails
Estimate: 30 minutes
Actual: 26 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        is_name = input(f"Is you name {name}? (Y/n) ")
        if is_name.upper() != "Y" and is_name != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    email_username = email.split('@')[0]
    name_parts = email_username.split('.')
    name = " ".join(name_parts).title()
    return name


main()
