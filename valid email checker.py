from email_validator import validate_email


def is_valid(email):
    return validate_email(email)


email_to_check = "saisriuthi@gmail.com"
if is_valid(email_to_check):
    print(f"The email {email_to_check} is valid")
else:
    print(f"The email {email_to_check} is not valid")
