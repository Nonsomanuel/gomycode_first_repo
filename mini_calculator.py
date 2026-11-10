#Creating a mini calculator using functions in Python
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2
firstnumber = float(input("Enter first number: "))
secondnumber = float(input("Enter second number: "))
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = input("Enter your choice (1/2/3/4): ")

if operation == '1':
    result = add(firstnumber, secondnumber)
    print(f"Result: {result}")
elif operation == '2':
    result = subtract(firstnumber, secondnumber)
    print(f"Result: {result}")
elif operation == '3':
    result = multiply(firstnumber, secondnumber)
    print(f"Result: {result}")
elif operation == '4':
    result = divide(firstnumber, secondnumber)
    print(f"Result: {result}")
else:
    print("Invalid operation selected.")
