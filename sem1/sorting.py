def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current position holds the minimum element
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the adjacent element is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no two elements were swapped in the inner loop, break
        if not swapped:
            break
    return arr


def insertion_sort(arr):
    n = len(arr)
    # Start from index 1 because the first element is already "sorted"
    for i in range(1, n):
        key = arr[i]  # Pick up the element we want to insert
        j = i - 1     # Set up the pointer to look at the element to its left
        
        # Keep shifting elements right as long as they are bigger than the key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Copy the larger number to the right
            j -= 1               # Move the pointer one step to the left
            
        # Drop the key into its correct final open spot
        arr[j + 1] = key
    return arr


# Example Usage
data = [64, 25, 12, 22, 11]
print("Selection Sorted:", selection_sort(data.copy()))
print("Bubble Sorted:   ", bubble_sort_optimized(data.copy()))
print("Insertion Sorted:", insertion_sort(data.copy()))
