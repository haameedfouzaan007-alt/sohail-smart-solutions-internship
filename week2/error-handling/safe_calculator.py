# Safe Calculator
# This program handles invalid input and division by zero without crashing.

while True:
    print("\n===== Safe Calculator =====")
    print("Supported operations: +, -, *, /")
    print("Type 'quit' anytime to exit.")

    # Get first number
    first_input = input("Enter first number: ")

    if first_input.lower() == "quit":
        print("Exiting calculator. Goodbye!")
        break

    try:
        first_number = float(first_input)
    except ValueError:
        print("Invalid number entered. Please try again.")
        continue

    # Get second number
    second_input = input("Enter second number: ")

    if second_input.lower() == "quit":
        print("Exiting calculator. Goodbye!")
        break

    try:
        second_number = float(second_input)
    except ValueError:
        print("Invalid number entered. Please try again.")
        continue

    # Get operation
    operation = input("Enter operation (+, -, *, /): ")

    if operation.lower() == "quit":
        print("Exiting calculator. Goodbye!")
        break

    # Perform calculation
    if operation == "+":
        result = first_number + second_number
        print("Result:", result)

    elif operation == "-":
        result = first_number - second_number
        print("Result:", result)

    elif operation == "*":
        result = first_number * second_number
        print("Result:", result)

    elif operation == "/":
        if second_number == 0:
            print("Cannot divide by zero. Please try again.")
        else:
            result = first_number / second_number
            print("Result:", result)

    else:
        print("Invalid operation. Please use +, -, *, or /.")