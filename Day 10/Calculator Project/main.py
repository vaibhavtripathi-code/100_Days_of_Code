from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

def calculation(n1, n2, operation):
    if operation == "+":
        return add(n1, n2)
    elif operation == "-":
        return subtract(n1, n2)
    elif operation == "*":
        return multiply(n1, n2)
    elif operation == "/":
        return divide(n1, n2)
    else:
        return "Invalid operation"


continued = False
keeprunning = True
number1 = 0
result = 0

while keeprunning:
    if not continued:
        number1 = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        number2 = float(input("Enter the second number: "))
        result = calculation(number1, number2, operation)
    else:
        number1 = result
        operation = input("Enter the operation (+, -, *, /): ")
        number2 = float(input("Enter the next number: "))
        result = calculation(number1, number2, operation)

    print(f"{number1} {operation} {number2} = {result}")

    cont = input(f"Type 'y' to continue calculating with {result}, 'n' to start new, or 'exit' to quit: ").lower()

    if cont == "y":
        continued = True
    elif cont == "n":
        continued = False
    else:
        keeprunning = False