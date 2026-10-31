import random
import time
from math import floor

# =====================================================================
# 1. STABLE COUNTING SORT (Slides 24, 27)
# =====================================================================
def stable_counting_sort(A, k):
    """
    Sorts array A stably assuming integer keys lie in range [0..k].
    Time: Theta(n + k), Auxiliary Space: Theta(n + k)
    """
    n = len(A)
    C = [0] * (k + 1)      # Phase 1: Initialize count array to all zeros
    B = [0] * n            # Empty output array to preserve record stability
    
    # Phase 1: Count frequencies
    for j in range(n):
        C[A[j]] += 1
        
    # Phase 2: Compute cumulative prefix sums
    for v in range(1, k + 1):
        C[v] = C[v] + C[v - 1]
        
    # Phase 3: Place records right-to-left (essential for stability!)
    for j in range(n - 1, -1, -1):
        v = A[j]
        B[C[v] - 1] = A[j]
        C[v] -= 1
        
    return B


# =====================================================================
# 2. LSD RADIX SORT (Slides 39, 42)
# =====================================================================
def stable_counting_sort_by_digit(A, position, b):
    """Stable counting sort subroutine configured for a specific base-b digit position."""
    n = len(A)
    C = [0] * b
    B = [0] * n
    
    # Digit extraction formula: digit(x, p) = floor(x / b^p) mod b
    get_digit = lambda x: (x // (b ** position)) % b
    
    for j in range(n):
        C[get_digit(A[j])] += 1
        
    for v in range(1, b):
        C[v] = C[v] + C[v - 1]
        
    for j in range(n - 1, -1, -1):
        v = get_digit(A[j])
        B[C[v] - 1] = A[j]
        C[v] -= 1
        
    # Overwrite original array with this pass's stable sorted arrangement
    for i in range(n):
        A[i] = B[i]

def lsd_radix_sort(A, d, b=10):
    """
    Sorts array A using Least Significant Digit first approach.
    Time: Theta(d(n + b)), Auxiliary Space: Theta(n + b)
    """
    # Sequentially pass through each digit slot from right to left
    for position in range(d):
        stable_counting_sort_by_digit(A, position, b)


# =====================================================================
# 3. BUCKET SORT (Slides 48, 51)
# =====================================================================
def insertion_sort(bucket):
    """Helper local-sorting routine recommended for short bucket sizes."""
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(A):
    """
    Sorts array A assuming inputs are uniformly distributed in [0, 1).
    Time: Expected Theta(n), Worst-case: Theta(n^2)
    """
    n = len(A)
    if n <= 1:
        return A
        
    # Create empty lists B[0..n-1]
    B = [[] for _ in range(n)]
    
    # Distribute elements into buckets based on floor(n * x)
    for x in A:
        i = floor(n * x)
        # Boundary check safeguard for exactly 1.0 if it slips into dataset
        if i >= n: 
            i = n - 1
        B[i].append(x)
        
    # Sort individual buckets locally using insertion sort
    for i in range(n):
        insertion_sort(B[i])
        
    # Concatenate B[0], B[1], ..., B[n-1] back into a single list
    output = []
    for bucket in B:
        output.extend(bucket)
        
    return output


# =====================================================================
# 4. EXECUTION & VERIFICATION WITH TIME.PERF_COUNTER()
# =====================================================================
if __name__ == "__main__":
    random.seed(42)  # For deterministic reproducibility
    
    print("--- 1. Testing Counting Sort ---")
    # Grayscale-like integer tokens (k=255 universe)
    counting_input = [random.randint(0, 255) for _ in range(100)]
    start = time.perf_counter()
    counting_output = stable_counting_sort(counting_input, k=255)
    end = time.perf_counter()
    print(f"Time taken: {(end - start) * 1000:.4f} ms")
    print(f"Sorted sequence (First 10): {counting_output[:10]}\n")
    
    print("--- 2. Testing Radix Sort (LSD) ---")
    # 3-digit integer keys (d=3, base b=10)
    radix_input = [random.randint(100, 999) for _ in range(100)]
    start = time.perf_counter()
    lsd_radix_sort(radix_input, d=3, b=10)
    end = time.perf_counter()
    print(f"Time taken: {(end - start) * 1000:.4f} ms")
    print(f"Sorted sequence (First 10): {radix_input[:10]}\n")
    
    print("--- 3. Testing Bucket Sort ---")
    # Float values uniformly mapped in range [0, 1)
    bucket_input = [random.random() for _ in range(100)]
    start = time.perf_counter()
    bucket_output = bucket_sort(bucket_input)
    end = time.perf_counter()
    print(f"Time taken: {(end - start) * 1000:.4f} ms")
    print(f"Sorted sequence (First 5): {[round(num, 4) for num in bucket_output[:5]]}\n")
