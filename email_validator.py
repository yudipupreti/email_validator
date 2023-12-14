import re
from email_validator import validate_email, EmailNotValidError

def is_valid_password(password):
    if len(password) < 8 or len(password) > 20:
        return False
    if "!" not in password and "#" not in password:
        return False
    return True

attempts = 3

while attempts > 0:
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == "" or password == "":
        print("Email or password is empty")
    else:
        try:
            email_info = validate_email(email, check_deliverability=True)
            email = email_info["email"]
            if is_valid_password(password):
                print("Logged in")
                print("Access granted")
                break
            else:
                print("Enter password again")
        except EmailNotValidError as e:
            print(str(e))

    attempts -= 1
    if attempts == 0:
        print("Id Blocked")