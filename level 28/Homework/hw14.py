# Create a list of odd numbers from 30 to 50
odd_numbers = [i for i in range(30, 51) if i % 2 != 0]

# Print the list of odd numbers
print("Odd numbers from 30 to 50:", odd_numbers)

# Sort the list to find the smallest elements
sorted_odd_numbers = sorted(odd_numbers)

# Calculate the sum of the three smallest elements
sum_of_smallest_three = sum(sorted_odd_numbers[:3])

# Print the sum
print("Sum of the three smallest elements:", sum_of_smallest_three)
