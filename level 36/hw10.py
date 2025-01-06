def is_prime(number):
    """
    Checks if a number is prime.
    
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

def filter_prime_numbers(numbers):
    """
    Filters out and returns only the prime numbers from a given list.
    
    Parameters:
        numbers (list): The list of numbers.
        
    Returns:
        list: A list containing only prime numbers.
    """
    return [num for num in numbers if is_prime(num)]

# Example usage
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime_numbers(my_numbers)
print(f"Prime numbers in the list: {prime_numbers}")
