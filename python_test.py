a = float(input("Enter number (a): "))
b = float(input("Enter number (b): "))
operations = input("Enter a operation (+, -, *, /)")


if operations == ("+"):
    print("The chosen operation is + and this is the answer", (a + b))
elif operations == ("-"):
    print("The chosen operation is - and this is the answer", (a - b))
elif operations == ("*"):
    print("The chosen operation is * and this is the answer", (a * b))
elif operations == ("/"):
    print("The chosen operation is / and this is the answer", (a / b))
else:
    print("ERROR")





