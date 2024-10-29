# List to store registered users
users = []

while True:
    print("\n--- User Registration ---")

    # Get username
    username = input("Enter a username: ")

    # Check for duplicate usernames
    if username in [user[0] for user in users]:
        print("Username already taken. Please choose another.")
        continue

    # Get email
    email = input("Enter your email: ")

    # Get password
    password = input("Enter a password: ")

    # Register the user
    users.append((username, email, password))  # Store as a tuple

    print("Registration successful!")

    # Check if the user wants to register another account
    another = input("Do you want to register another user? (yes/no): ").strip().lower()
    if another != 'yes':
        break

# Display registered users
print("\nRegistered Users:")
for user in users:
    print(f"Username: {user[0]}, Email: {user[1]}")
