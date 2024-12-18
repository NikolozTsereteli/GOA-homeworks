def compare_numbers():
    # Accept the first number
    num1 = float(input("Enter the first number: "))
    
    # Accept the second number
    num2 = float(input("Enter the second number: "))
    
    # Compare the two numbers and print the larger one
    if num1 > num2:
        print(f"The larger number is: {num1}")
    elif num2 > num1:
        print(f"The larger number is: {num2}")
    else:
        print("Both numbers are equal.")

# Call the function
compare_numbers()
