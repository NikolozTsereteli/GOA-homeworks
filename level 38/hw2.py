def find_max(numbers):
    """
    Returns the largest number in a list.
    
    Parameters:
        numbers (list): A list of numbers.
        
    Returns:
        int or float: The largest number in the list.
    """
    if not numbers:  # Check if the list is empty
        return "The list is empty."
    return max(numbers)

# Example usage
my_list = [3, 7, 2, 9, 4, 15, 6]
largest_number = find_max(my_list)
print(f"The largest number in the list is: {largest_number}")
