def is_even():
    # Accept a number as input
    num = int(input("Enter a number: "))
    
    # Check if the number is even
    return num % 2 == 0

# Example usage
result = is_even()
print("The number is even:", result)
