# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    # If even, divide by two
    result = number / 2
    print(f"The number is even. {number} divided by 2 is: {result}")
else:
    # If odd, multiply by three and add one
    result = number * 3 + 1
    print(f"The number is odd. {number} multiplied by 3 and added 1 is: {result}")
