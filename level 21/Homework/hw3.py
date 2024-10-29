# Get user input and convert it to an integer
user_number = int(input("Enter a number: "))

# Initialize sum variable and count of numbers
sum_of_natural_numbers = 0
count_of_numbers = 0

# Loop to calculate the sum and count of natural numbers up to the entered number
for i in range(1, user_number + 1):
    sum_of_natural_numbers += i
    count_of_numbers += 1

# Calculate the arithmetic mean
if count_of_numbers > 0:
    arithmetic_mean = sum_of_natural_numbers / count_of_numbers
else:
    arithmetic_mean = 0

# Print the result
print("The arithmetic mean of all natural numbers up to", user_number, "is:", arithmetic_mean)
