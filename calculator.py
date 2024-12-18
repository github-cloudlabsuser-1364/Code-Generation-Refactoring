# Create a basic calculator 
def calculator():
    print("Welcome to the basic calculator.")
    while True:
        user_input = input("Enter the first number (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        try:
            num1 = float(user_input)
        except ValueError:
            print("Invalid number.")
            continue
        operator = input("Enter an operation (+, -, *, /): ")
        if operator not in ('+', '-', '*', '/'):
            print("Invalid operator.")
            continue
        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid number.")
            continue
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Cannot divide by zero.")
                continue
            result = num1 / num2
        print(f"Result: {result}")

calculator()