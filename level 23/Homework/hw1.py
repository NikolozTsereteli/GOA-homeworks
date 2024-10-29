# Perform mathematical operations on pairs of numbers from 0 to 100
for i in range(101):  # First number
    for j in range(101):  # Second number
        # Addition
        addition_result = i + j
        print(f"{i} + {j} = {addition_result}")

        # Subtraction
        subtraction_result = i - j
        print(f"{i} - {j} = {subtraction_result}")

        # Multiplication
        multiplication_result = i * j
        print(f"{i} * {j} = {multiplication_result}")

        # Division
        if j != 0:  # Avoid division by zero
            division_result = i / j
            print(f"{i} / {j} = {division_result}")
        else:
            print(f"{i} / {j} = Undefined (division by zero)")

        print()  # Print a newline for better readability

