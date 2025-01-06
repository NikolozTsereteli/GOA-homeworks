def get_first_element(lst):
    """
    Returns the first element of the given list.
    
    Parameters:
        lst (list): The list from which to retrieve the first element.
        
    Returns:
        The first element of the list.
    """
    if lst:
        return lst[0]
    else:
        return None  # Return None if the list is empty

# Example usage
my_list = [10, 20, 30, 40]
first_element = get_first_element(my_list)
print(f"The first element is: {first_element}")
