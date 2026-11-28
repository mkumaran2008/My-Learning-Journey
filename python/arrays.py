numbers = [10, 20, 30, 40, 50]

# Access an element
print("First element:", numbers[0])

# Update an element
numbers[1] = 25

# Add an element
numbers.append(60)

# Traverse the list
print("All elements:")

for number in numbers:
    print(number)

# Calculate the total
total = 0

for number in numbers:
    total += number

print("Total:", total)
