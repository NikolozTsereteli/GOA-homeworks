def are_equal(num1, num2):
    """
    Checks if two numbers are equal.
    
    Parameters:
        num1 (int or float): The first number.
        num2 (int or float): The second number.
        
    Returns:
        bool: True if the numbers are equal, False otherwise.
    """
    return num1 == num2

# Example usage
number1 = 5
number2 = 5
if are_equal(number1, number2):
    print(f"{number1} and {number2} are equal.")
else:
    print(f"{number1} and {number2} are not equal.")
