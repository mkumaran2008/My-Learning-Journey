numbers = [10, 20, 30, 40, 50, 60, 70]

target = 50

low = 0
high = len(numbers) - 1

found_index = -1

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == target:
        found_index = mid
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

if found_index != -1:
    print("Element found at index:", found_index)

else:
    print("Element not found")
