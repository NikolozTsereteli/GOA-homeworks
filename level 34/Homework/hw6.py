def celsius_to_fahrenheit():
    # Accept the temperature in Celsius
    celsius = float(input("Enter the temperature in Celsius: "))
    
    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    
    # Print the result
    print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")

# Call the function
celsius_to_fahrenheit()