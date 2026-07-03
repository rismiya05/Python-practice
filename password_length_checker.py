password=input("Enter your password:")
valid=True
if password.isdigit():
    print("Password should not be only numbers.")
    valid=False
if password.isalpha():
    print("Password should not be only letters.")
    valid=False
if password.isalnum():
    print("Password should contain at least one special character.")
    valid=False
if len(password) < 8:
    print("Password should be at least 8 characters long.")
    valid=False
if len(password) > 20:
    print("Password should not be more than 20 characters long.")
    valid=False
if password.islower():
    print("Password should contain at least one uppercase letter.")
    valid=False
if valid:
    print("Password is valid.")