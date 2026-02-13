import random


def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = "".join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Enter the desired password length: "))
password = generate_password(length)

with open("passwords.txt", "w") as file:
    file.write(password)

print(f"Generated password: {password}")

# This code generates a random password of a specified length and saves it to a file called "passwords.txt".
# The password includes a mix of uppercase letters, lowercase letters, digits, and special characters.
  