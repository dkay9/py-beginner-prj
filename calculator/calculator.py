#create functioons for the operators 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#create variables for collecting user inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

#logic for deciding which function is called based on user input
if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
        exit()
    result = divide(num1, num2)
else:
    print("Invalid operator")
    exit()

#show result
print(f"Result: {result}")