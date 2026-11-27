# Store numbers in a list
numbers = [10, 20, 30, 40, 50]

# Display all numbers
print("Numbers:", numbers)

# Find the largest number
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number:", largest)

# Find a particular number
target = 30

for number in numbers:
    if number == target:
        print("Number found:", target)
        break
