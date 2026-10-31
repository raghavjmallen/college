import random
import time
from math import floor

# ==========================================
# GENERATE RANDOM INPUT DATASET
# ==========================================
random.seed(42)  
original_arr = [random.randint(10, 999) for _ in range(100)]

# ==========================================
# SORTING ALGORITHMS
# ==========================================
def counting_sort(arr):
    if not arr: 
        return
    max_val, min_val = max(arr), min(arr)
    range_of_elements = max_val - min_val + 1
    
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)
    
    for num in arr:
        count_arr[num - min_val] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1
    for i in range(len(arr)):
        arr[i] = output_arr[i]

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        count[(arr[i] // exp) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort_lsd(arr):
    if not arr: 
        return
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    if n <= 1: 
        return
        
    max_val, min_val = max(arr), min(arr)
    val_range = (max_val - min_val) / n if max_val != min_val else 1
    
    buckets = [[] for _ in range(n)]
    for num in arr:
        bucket_idx = floor((num - min_val) / val_range)
        if bucket_idx >= n:
            bucket_idx = n - 1
        buckets[bucket_idx].append(num)
        
    k = 0
    for bucket in buckets:
        insertion_sort(bucket) 
        for num in bucket:
            arr[k] = num
            k += 1

# ==========================================
# PERFORMANCE BENCHMARKING & EXECUTION
# ==========================================
if __name__ == "__main__":
    print(f"Original Array Sample (First 15 elements):\n{original_arr[:15]}...\n")
    print("-" * 65)
    
    # 1. Benchmark & Print Counting Sort
    arr_counting = original_arr.copy()
    start = time.perf_counter()
    counting_sort(arr_counting)
    end = time.perf_counter()
    time_counting = (end - start) * 1000  
    print(f"Counting Sort Time  : {time_counting:.4f} ms")
    print(f"Counting Sort Output: {arr_counting[:15]}...\n")
    
    # 2. Benchmark & Print Radix Sort
    arr_radix = original_arr.copy()
    start = time.perf_counter()
    radix_sort_lsd(arr_radix)
    end = time.perf_counter()
    time_radix = (end - start) * 1000
    print(f"Radix Sort Time     : {time_radix:.4f} ms")
    print(f"Radix Sort Output   : {arr_radix[:15]}...\n")
    
    # 3. Benchmark & Print Bucket Sort
    arr_bucket = original_arr.copy()
    start = time.perf_counter()
    bucket_sort(arr_bucket)
    end = time.perf_counter()
    time_bucket = (end - start) * 1000
    print(f"Bucket Sort Time    : {time_bucket:.4f} ms")
    print(f"Bucket Sort Output  : {arr_bucket[:15]}...\n")
    
    print("-" * 65)
    # Summary Table
    print(f"{'Algorithm':<20} | {'Execution Time (ms)':<20}")
    print("-" * 43)
    print(f"{'Counting Sort':<20} | {time_counting:.4f} ms")
    print(f"{'Radix Sort (LSD)':<20} | {time_radix:.4f} ms")
    print(f"{'Bucket Sort':<20} | {time_bucket:.4f} ms")
