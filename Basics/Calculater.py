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