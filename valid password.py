is_valid_password = lambda password: (
    len(password) >= 8 and
    any(char.isupper() for char in password) and
    any(char.islower() for char in password) and
    any(char.isdigit() for char in password) and
    any(char in '!@#$%^&*()_-+={}[]|:;"<>,.?/~`' for char in password)
)

# Example usage:
password = "StrongP@ssw0rd"
result = is_valid_password(password)
print(f"The password '{password}' is {'valid' if result else 'invalid'}.")