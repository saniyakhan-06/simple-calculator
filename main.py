def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
try:
    operator = input("Enter the operation to be perfromed (add/sub/mul/div): ").strip().lower()


    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))


    if operator == "add":
        result = addition(a, b)
    elif operator == "sub":
        result = subtraction(a, b)
    elif operator == "mul":
        result = multiplication(a, b)
    elif operator == "div":
        result = division(a, b)
    else:
        print("Invalid operation")
        result = None
    if result is not None:
        print("Result: ", result)
except ValueError as ve:
    print("Error", ve)
except ValueError as e:
    print("Unexpected error", e)



