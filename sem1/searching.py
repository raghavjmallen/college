def linear_search(arr, target):
    n = len(arr)
    # Scan sequentially from index 0 to n-1
    for i in range(n):
        if arr[i] == target:
            return i  # Target found! Return its index position.
            
    return -1  # Loop ended and found nothing.


def binary_search(arr, target):
    # Set up the two boundary markers
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate the middle index of the current boundaries
        mid = low + (high - low) // 2  # '//' performs integer division

        if arr[mid] == target:
            return mid  # Target found right in the middle!
        elif arr[mid] < target:
            # Target is in the right half, move the lower wall up
            low = mid + 1
        else:
            # Target is in the left half, pull the upper wall down
            high = mid - 1
            
    return -1  # Target does not exist in the array.


# --- Example Usage ---

# 1. Linear Search Sample (Works on unsorted data)
unsorted_data = [64, 25, 12, 22, 11]
target1 = 22

result1 = linear_search(unsorted_data, target1)
print(f"Linear Search: Found {target1} at index {result1}")


# 2. Binary Search Sample (Data MUST be sorted first)
sorted_data = [11, 12, 22, 25, 64]
target2 = 25

result2 = binary_search(sorted_data, target2)
print(f"Binary Search: Found {target2} at index {result2}")
