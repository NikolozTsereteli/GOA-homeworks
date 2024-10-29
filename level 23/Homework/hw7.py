# Start an infinite loop
while True:
    # Ask the user for their name
    name = input("Please enter your name (or type 'quit' to exit): ")

    # Check if the user wants to quit
    if name.lower() == "quit":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop if the user types "quit"
    else:
        print(f"Hello, {name}!")  # Greet the user
