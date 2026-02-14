with open("account_manager.txt", "w") as file:                       # Create the file if it doesn't exist and write the header
    file.write("ID          USERNAME           PASSWORD\n")

with open("account_manager.txt", "r") as file:
    existing_accounts = [account.strip() for account in file.readlines()[1:]]  # Skip the header line


username = input("Enter the 10 digit username: ")                                  # Get the username input from the user
if len(username) >10:
    print("Username should not exceed 10 characters. Please try again.")  # Check if the username exceeds 10 characters and prompt the user to try again if it does
    exit()
elif username == "":
    print("Username cannot be empty. Please try again.")                   # Check if the username is empty and prompt the user to try again if it is
    exit()
elif len(username) == 10:
    print("Username is valid.")                                                   # If the username is valid, print a confirmation message
elif len(username) < 10:
    print("username is invalid. Please try again.")                                                   # If the username is invalid, print an error message and prompt the user to try again
    exit()
    
if any(username in account for account in existing_accounts):
    print("Username already exists. Please choose a different username.")
    exit()

password = input("Enter the password: ")

def auto_increment():                
    with open ("account_manager.txt", "r") as f:
        num = f.readlines()
        X = len(num)
    return str(X)
    


with open("account_manager.txt", "a") as file:
    file.write(f"ID{auto_increment()}){' '*8}{username}{' '*10}{password}\n")
    
print("Account created successfully!!!")
print("Your account details are:")
print(f"ID: ID{len(existing_accounts)+1}")
print(f"Username: {username}")
print(f"Password: {password}")


# This code creates a simple account manager that allows users to create accounts with a username with length 10 and password. 
# It checks for duplicate usernames and ensures that the username does not exceed 10 characters. 
# The account details are stored in a text file called "account_manager.txt". 
# Each account is assigned a unique ID that auto-increments based on the number of existing accounts.