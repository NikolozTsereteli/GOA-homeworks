def check_number():
    # Accept a number as input
    num = int(input("Enter a number: "))
    
    # Check if the number is between 1 and 10
    if 1 <= num <= 10:
        print(f"The number is: {num}")
    else:
        print("Invalid number")

# Call the function
check_number()
