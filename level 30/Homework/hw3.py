# Create an empty list
numbers = []

# Prompt the user to enter a number
user_input = int(input("Enter a number: "))

# Use a for loop to add numbers from 1 to the user's number
for i in range(1, user_input + 1):
    numbers.append(i)

# Print the final list
print(numbers)
