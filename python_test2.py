def add(a,b):
    return(a+b)


def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def division(a,b):
    return(a/b)

a = float(input("Enter a numebr (a): "))
b = float(input("Enter a number (b): "))
operation = str(input("Enter a operation [+, -, *, /]: "))

if operation == ("+"):
    add
    print("The answer is:", add)
elif operation == ("-"):
    subtract
    print("The answer is:", subtract)
elif operation == ("*"):
    multiply
    print("The answer is:", multiply)
elif operation == ("/"):
    division
    print("The answer is:", division)
else:
    print("ERROR!")