# A list of numbers
numbers = [23, 56, 12, 78, 90, 34, 67]

# Initialize the variable to store the largest number
largest = numbers[0]  # Assume the first number is the largest initially

# Iterate through the list to find the largest number
for num in numbers:
    if num > largest:
        largest = num  # Update the largest number if a bigger number is found

# Print the largest number
print("The largest number in the list is:", largest)
