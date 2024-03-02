# Open the file
with open('file.txt', 'r') as file:
    # Read lines from the file
    lines = file.readlines()

# Initialize an empty array to store the first elements
first_elements = []

# Iterate through each line
for line in lines:
    # Remove parentheses and split the line by commas
    values = line.strip('()\n').split(',')
    # Convert the first element to a float
    first_element = float(values[0])
    # Append the first element to the array
    first_elements.append(first_element)

# Print the array of first elements
print(first_elements)
