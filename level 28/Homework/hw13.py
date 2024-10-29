# Create a list of multiples of 4 from 0 to 20
multiples_of_4 = [i for i in range(21) if i % 4 == 0]

# Print the list of multiples
print("Multiples of 4 from 0 to 20:", multiples_of_4)

# Print the largest multiple of 4
largest_multiple = max(multiples_of_4)
print("Largest multiple of 4:", largest_multiple)
