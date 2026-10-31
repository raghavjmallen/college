def merge(arr, l, m, r):
    """Merges two sorted subarrays: arr[l..m] and arr[m+1..r]"""
    left_copy = arr[l:m + 1]
    right_copy = arr[m + 1:r + 1]
    
    i = 0  
    j = 0  
    k = l  
    
    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1
        
    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1
        
    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1

def bottom_up_sort(arr):
    """Sorts the array iteratively using Bottom-Up Merge Sort"""
    n = len(arr)
    width = 1
    
    # Process subarrays of size 1, 2, 4, 8, etc.
    while width < n:
        # Pick starting points for different subarrays of the current width
        for l in range(0, n, 2 * width):
            m = min(l + width - 1, n - 1)
            r = min(l + 2 * width - 1, n - 1)
            
            # Only merge if a valid second subarray exists
            if m < r:
                merge(arr, l, m, r)
                
        # Double the subarray width for the next pass
        width *= 2

# ---- EXECUTION BLOCK ----
arr = [3, 8, 4, 5, 12, 76, 66, 90, 14, 65, 45, 20, 90]

print("Before sorting:", arr)

# Execute the iterative bottom-up sort
bottom_up_sort(arr) 

print("After sorting: ", arr)
