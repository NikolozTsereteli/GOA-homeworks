def is_positive(number):
    """
    Checks if a number is greater than zero.
    
    Parameters:
        number (int or float): The number to check.
        
    Returns:
        bool: True if the number is greater than zero, False otherwise.
    """
    return number > 0

# Example usage
num = 5
if is_positive(num):
    print(f"{num} is greater than zero.")
else:
    print(f"{num} is not greater than zero.")
