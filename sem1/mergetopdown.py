def merge(arr, l, m, r):
    """Merges two sorted subarrays: arr[l..m] and arr[m+1..r]"""
    # Create copies of the left and right subarrays
    left_copy = arr[l:m + 1]
    right_copy = arr[m + 1:r + 1]
    
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged array
    
    # Merge the temporary arrays back into arr[l..r]
    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1
        
    # Copy any remaining elements of left_copy
    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1
        
    # Copy any remaining elements of right_copy
    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1
def merge_sort_top_down(arr, l, r):
    """Sorts arr[l..r] using Top-Down Merge Sort"""
    if l >= r:
        return
        
    m = l + (r - l) // 2
    
    # Recursively divide the left and right halves
    merge_sort_top_down(arr, l, m)
    merge_sort_top_down(arr, m + 1, r)
    
    # Merge the sorted halves
    merge(arr, l, m, r)

# Wrapper function for ease of use
def top_down_sort(arr):
    merge_sort_top_down(arr, 0, len(arr) - 1)
arr=[3,8,4,5,12,76,66,90,14,65,45,20,90]
# 2. CALL THE FUNCTION (This was missing!)
top_down_sort(arr)

print(arr)
