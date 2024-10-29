# Get user input and convert it to an integer
user_number = int(input("Enter a number: "))

# Initialize sum variable
sum_of_natural_numbers = 0

# Loop to calculate the sum of natural numbers up to the entered number
for i in range(1, user_number + 1):
    sum_of_natural_numbers += i

# Print the result
print("The sum of all natural numbers up to", user_number, "is:", sum_of_natural_numbers)
