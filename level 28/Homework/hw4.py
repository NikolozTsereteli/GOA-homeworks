# Create a list of twenty different numbers
numbers = [3, 12, 8, 15, 22, 7, 4, 19, 2, 11, 10, 6, 5, 13, 18, 21, 1, 9, 14, 16]

# Print the even numbers less than 10
print("Even numbers less than 10:")
for number in numbers:
    if number < 10 and number % 2 == 0:  # Check if the number is less than 10 and even
        print(number)
