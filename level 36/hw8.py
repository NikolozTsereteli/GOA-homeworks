def is_prime(number):
    """
    Checks if a number is a prime number.
    
    Parameters:
        number (int): The number to check.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
num = 29
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

