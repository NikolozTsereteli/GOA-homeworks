# Create a list of numbers from 1 to 20
numbers = list(range(1, 21))

# Loop through each number in the list
for number in numbers:
    # Check if the number is even or odd
    if number % 2 == 0:
        label = "even"
    else:
        label = "odd"
    
    # Print the number and its label
    print(f"{number} is {label}.")
