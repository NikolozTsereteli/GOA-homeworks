# Get user input and convert it to an integer
user_number = int(input("Enter a number: "))

# Loop through numbers from 1 to the entered number
for i in range(1, user_number + 1):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
