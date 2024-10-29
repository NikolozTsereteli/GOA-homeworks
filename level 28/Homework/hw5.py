# Create a list of twenty different numbers
numbers = [5, 12, 29, 15, 22, 33, 7, 24, 42, 11, 10, 27, 5, 38, 19, 50, 1, 9, 63, 45]

# Print the numbers above 20 that are multiples of 3
print("Numbers above 20 that are multiples of 3:")
for number in numbers:
    if number > 20 and number % 3 == 0:  # Check if the number is above 20 and a multiple of 3
        print(number)
