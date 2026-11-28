numbers = [15, 8, 42, 23, 5, 30]

maximum = numbers[0]
minimum = numbers[0]

for number in numbers:

    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

print("Array:", numbers)
print("Maximum element:", maximum)
print("Minimum element:", minimum)
