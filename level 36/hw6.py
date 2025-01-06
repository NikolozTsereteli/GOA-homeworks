def print_squares(numbers):
    """
    Prints the square of each number in the given list.
    
    Parameters:
        numbers (list): A list of numbers.
    """
    for number in numbers:
        print(f"{number} squared is {number ** 2}")

# Example usage
my_numbers = [1, 2, 3, 4, 5]
print_squares(my_numbers)
