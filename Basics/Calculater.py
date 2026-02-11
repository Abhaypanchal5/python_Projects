num1 = int(input("Enter the first number: "))
op = input("Enter the operator (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid operator.")
    exit()

print("Result:", result)

# this is a simple calculator program that takes two numbers and an operator as input from the user, 
# performs the specified operation, and outputs the result. 
# The program handles addition, subtraction, multiplication, and division, 
# and also checks for division by zero to prevent errors.