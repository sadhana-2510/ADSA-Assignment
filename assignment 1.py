def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                swapped = True
        if not swapped:
            break  # If no two elements were swapped in an iteration, the list is already sorted.
    return arr

# Input data
input_array = [5, 2, 9, 1, 5, 6]

# Sorting the array using Bubble Sort
sorted_array = bubble_sort(input_array.copy())  # Create a copy to preserve the original array

print("Sorted Array:", sorted_array)
