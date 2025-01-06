def find_minimum(a, b):
    """
    Returns the minimum of two numbers.
    
    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.
        
    Returns:
        int or float: The smaller of the two numbers.
    """
    return a if a < b else b

# Example usage
num1 = 10
num2 = 20
minimum = find_minimum(num1, num2)
print(f"The minimum of {num1} and {num2} is {minimum}.")
