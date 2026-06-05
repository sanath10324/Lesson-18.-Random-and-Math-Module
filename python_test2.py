def add(a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)

try:
    num1 = float(input("Enter num1:"))
    num2 = float(input("Enter num2:"))

    print("\nChoose a Operation: ")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")

    operation = input("Choose your operation: ")

    if operation == "+":
        print("Answer =", add(num1, num2))

    elif operation == "-":
        print("Answer =", subtract(num1, num2))

    elif operation == "*":
        print("Answer =", multiply(num1, num2))

    elif operation == "/":
        print("Answer =", divide(num1, num2))

    else:
      print("Invalid operation entered.")

except ValueError:
    print("Value Error: Please enter numbers only.")

except ZeroDivisionError:
    print("Zero Division Error: Cannot divide by zero.")