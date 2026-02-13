with open("Email.txt", "w") as f:    # This line opens a file named "Email.txt" in write mode ("w"). If the file does not exist, it will be created. If it already exists, its contents will be overwritten.
    f.write("Email List\n")          # Run this code once to create the file and add the header "Email List" to it. After running this code, you can comment it out or remove it to prevent overwriting the file in future runs.

def auto_increment():                # This line defines a function named "auto_increment". This function will be used to generate a unique identifier for each email entry in the list.(file should be empty)
    with open ("Email.txt", "r") as f:
        num = f.readlines()
        X = len(num)
    return str(X)
    
key = F"ID-{auto_increment()}"          
name= input("Enter the name: ")
Value = input("Enter the email: ")
if Value == "":
    Value = f"{name}@gmail.com"           # This line checks if the user has entered an email address. If the input is empty (""), it generates a default email address using the provided name and appending "@gmail.com" to it. The generated email address is then stored in the variable "Value".
    print(f"Generated email: {Value}")
if Value.count("@") != 1 or Value.count(".") == 0:
    print("Invalid email address. Please enter a valid email.")
else:
    with open("Email.txt", "a") as f:           # This line opens the "Email.txt" file in append mode ("a"). This means that new data will be added to the end of the file without overwriting existing content.
        f.write(f"{key}) {name}: {Value}\n")
    print(f"Data saved successfully with key: {key}")
    print(f"you entered: {name} and {Value}")    

    
    