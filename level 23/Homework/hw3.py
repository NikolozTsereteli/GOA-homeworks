# Get user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Initialize sum and product variables
sum_result = 0
product_result = 1

# Using a for loop to calculate sum and product
for i in range(1):  # This loop will run once
    sum_result = num1 + num2  # Calculate the sum
    product_result = num1 * num2  # Calculate the product

# Output the results
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The product of {num1} and {num2} is: {product_result}")
