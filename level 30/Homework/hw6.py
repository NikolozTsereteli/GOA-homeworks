# Create a list containing 20 different numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Create two empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Use a for loop to filter even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)  # Add to the even list
    else:
        odd_numbers.append(num)   # Add to the odd list

# Print the even and odd lists
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
