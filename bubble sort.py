def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Example
numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original List:", numbers)
bubble_sort(numbers)
print("Sorted List:", numbers)
