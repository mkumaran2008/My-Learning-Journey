numbers = [12, 25, 37, 48, 59, 64]

target = 48

found = False

for index in range(len(numbers)):

    if numbers[index] == target:
        print("Element found!")
        print("Position:", index + 1)
        print("Index:", index)

        found = True
        break

if not found:
    print("Element not found")
