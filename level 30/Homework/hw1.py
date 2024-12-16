# Create a list with at least 10 names
names = [
    "Alexander",
    "Maria",
    "Elizabeth",
    "Christopher",
    "John",
    "Sophia",
    "Matthew",
    "Isabella",
    "William",
    "Charlotte"
]

# Create a filtered list to store names with length <= 10
filtered_names = []

# Use a for loop to filter the names
for name in names:
    if len(name) <= 10:
        filtered_names.append(name)

# Print the filtered list
print(filtered_names)
