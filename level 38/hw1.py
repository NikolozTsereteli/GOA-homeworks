def calculator():
    """
    A calculator that takes two numbers and an operation from the user, 
    performs the operation, and returns the result.
    """
    try:
        # Taking inputs from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Performing the operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operation."
        
        # Returning the result
        return f"The result of {num1} {operation} {num2} is: {result}"
    
    except ValueError:
        return "Error: Please enter valid numbers."

# Run the calculator
print(calculator())
