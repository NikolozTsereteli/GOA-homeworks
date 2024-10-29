# Get user input
user_input = int(input("Enter a number: "))

# Initialize sum variable
total_sum = 0

# Calculate the sum of all numbers up to the entered number
for i in range(1, user_input + 1):  # Start from 1 to user_input inclusive
    total_sum += i  # Add each number to the total_sum

# Output the result
print(f"The sum of all numbers up to {user_input} is: {total_sum}")
