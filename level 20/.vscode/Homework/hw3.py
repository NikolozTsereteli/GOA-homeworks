# Initialize sum variable
sum_of_multiples = 0

# Loop through numbers 1 to 100
for i in range(1, 101):
    if i % 5 == 0:
        sum_of_multiples += i
    else:
        continue  # Continue to the next iteration if not a multiple of 5

# Print the result
print("The sum of multiples of 5 from 1 to 100 is:", sum_of_multiples)
