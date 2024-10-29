# Start an infinite loop
while True:
    # Ask the user for a number
    number = float(input("Please enter a positive number: "))  # Convert input to float for generality

    # Check if the number is positive
    if number > 0:
        print(f"You entered a positive number: {number}")
        break  # Exit the loop if the number is positive
    else:
        print("That is not a positive number. Please try again.")
