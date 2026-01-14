try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")