import random
import string

print("Password Generator")
length = int(input("Enter the desired length of the password: "))
complexity = input("Enter complexity level (low/medium/high): ").lower()


uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
digits = "0123456789"
symbols = "!@#$%^&*()"

def generate_password(length, complexity):
    if complexity == "low":
        characters = uppercase + lowercase
    elif complexity == "medium":
        characters = uppercase + lowercase + string.digits 
    elif complexity == "high":
        characters = uppercase + lowercase + string.digits + symbols
    else:
        print("Invalid complexity level")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

    
password = generate_password(length, complexity)
if password:
    print("Generated Password: " + password)













