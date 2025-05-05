# Assignment-A3.I (Simplified Selection Sort)

# Take space-separated input and convert to float list
numbers = list(map(float, input("Enter numbers separated by space:\n").split()))

# Selection Sort
for i in range(len(numbers)):
    min_idx = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

# Print sorted result
print("Sorted numbers:", numbers)
