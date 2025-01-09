def find_min(numbers):
    """
    Returns the smallest number in a list.
    
    Parameters:
        numbers (list): A list of numbers.
        
    Returns:
        int or float: The smallest number in the list, or an error message if the list is empty.
    """
    if not numbers:  # Check if the list is empty
        return "The list is empty."
    return min(numbers)

# Example usage
my_list = [3, 7, 2, 9, 4, -5, 6]
smallest_number = find_min(my_list)
print(f"The smallest number in the list is: {smallest_number}")
