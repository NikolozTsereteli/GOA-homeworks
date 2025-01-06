def count_elements(lst):
    """
    Counts the number of elements in a list.
    
    Parameters:
        lst (list): The list whose elements are to be counted.
        
    Returns:
        int: The number of elements in the list.
    """
    return len(lst)

# Example usage
my_list = [1, 2, 3, 4, 5]
count = count_elements(my_list)
print(f"The list contains {count} elements.")
