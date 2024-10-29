# Create a list of numbers from 1 to 20
numbers = list(range(1, 21))

# Print the multiples of 3
print("Multiples of 3 from 1 to 20:")
for number in numbers:
    if number % 3 == 0:
        print(number)
