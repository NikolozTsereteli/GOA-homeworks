def get_alphabet_position(name):
    """
    Returns the position of the first letter of the name in the alphabet.
    
    Parameters:
        name (str): The name of the user.
        
    Returns:
        int or str: The position of the first letter in the alphabet, or an error message.
    """
    if not name:
        return "Error: The name is empty."
    
    first_letter = name[0].upper()  # Take the first letter and convert it to uppercase
    if 'A' <= first_letter <= 'Z':  # Check if it's a valid English alphabet letter
        position = ord(first_letter) - ord('A') + 1
        return f"The first letter '{first_letter}' is the {position}-th letter in the alphabet."
    else:
        return "Error: The first character is not a valid letter."

# Ask the user for their name
user_name = input("Enter your name: ").strip()
result = get_alphabet_position(user_name)
print(result)
