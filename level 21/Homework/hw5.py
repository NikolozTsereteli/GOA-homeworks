# Get user input and convert it to an integer
user_number = int(input("Enter a number: "))

# Loop through numbers from 1 to the entered number
print("Multiples of 5 up to", user_number, "are:")
for i in range(1, user_number + 1):
    if i % 5 == 0:
        print(i)
