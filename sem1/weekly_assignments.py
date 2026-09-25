import random
import time

# =====================================================================
# WEEK 3 ASSIGNMENT: SEARCH VARIANT & BENCHMARKING
# =====================================================================

def run_week_2_assignment():
    print("---- Phase 1: Initialization Starting ----", flush=True)
    # 1. Initialize list of size 100001 with random numbers and sort it
    size = 100001
    random_list = [random.randint(1, 1000000) for _ in range(size)]
    random_list = sorted(random_list)
    print("---- Phase 1: Initialization Completed ----\n", flush=True)

    target_value = 10000

    # 2. Linear Search implementation over even indices
    print("---- Phase 2: Linear Search Starting ----", flush=True)
    start_time = time.perf_counter()
    
    linear_result = -1
    for i in range(0, len(random_list), 2):
        # Optional: time.sleep(0.0001) # Uncomment to simulate expensive comparisons
        if random_list[i] == target_value:
            linear_result = i
            break
            
    end_time = time.perf_counter()
    linear_duration = end_time - start_time
    
    if linear_result != -1:
        print(f"Value found at even index: {linear_result}", flush=True)
    else:
        print("Value not found via Linear Search.", flush=True)
    print(f"Linear Search Execution Time: {linear_duration:.6f} seconds", flush=True)
    print("---- Phase 2: Linear Search Completed ----\n", flush=True)

    # 3. Binary Search implementation over even indices
    print("---- Phase 3: Binary Search Starting ----", flush=True)
    start_time = time.perf_counter()
    
    binary_result = -1
    lo = 0
    hi = len(random_list) - 1
    
    # Ensure hi starts at an even index
    if hi % 2 != 0:
        hi -= 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        # Force mid to be an even index
        if mid % 2 != 0:
            mid -= 1
            
        # If adjusting mid drops it below lo, the value is not in this range
        if mid < lo:
            break
            
        # Optional: time.sleep(0.0001) # Uncomment to simulate expensive comparisons
        if random_list[mid] == target_value:
            binary_result = mid
            break
        elif random_list[mid] < target_value:
            lo = mid + 2
        else:
            hi = mid - 2

    end_time = time.perf_counter()
    binary_duration = end_time - start_time

    if binary_result != -1:
        print(f"Value found at even index: {binary_result}", flush=True)
    else:
        print("Value not found via Binary Search.", flush=True)
    print(f"Binary Search Execution Time: {binary_duration:.6f} seconds", flush=True)
    print("---- Phase 3: Binary Search Completed ----\n", flush=True)


# =====================================================================
# WEEK 4 ASSIGNMENT: MATH, ITERATION & RECURSION
# =====================================================================

# Nth Fibonacci using iteration
def fibonacci_iterative(n):
    if n <= 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Nth Fibonacci using recursion
def fibonacci_recursive(n):
    if n <= 0: return 0
    elif n == 1: return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Fibonacci series till nth sequence
def fibonacci_series_sequence(n):
    series = []
    for i in range(n):
        series.append(fibonacci_iterative(i))
    return series

# Fibonacci series till nth value
def fibonacci_series_value(max_val):
    series = []
    i = 0
    while True:
        val = fibonacci_iterative(i)
        if val > max_val:
            break
        series.append(val)
        i += 1
    return series

# Check if a number is a "Nice Number"
def is_nice_number(num):
    num_str = str(num)[::-1] # Reverse to process from right-to-left (ones, tens, hundreds...)
    for idx, char in enumerate(num_str):
        digit = int(char)
        if idx % 2 == 0:  # Ones (0), Hundreds (2), Ten-Thousands (4)...
            if digit % 2 == 0:
                return False # Must be odd
        else:             # Tens (1), Thousands (3)...
            if digit % 2 != 0:
                return False # Must be even
    return True

# Show if the number is a power of 2 or 3
def check_power_of_2_or_3(num):
    if num <= 0:
        return "Not a power of 2 or 3"
        
    # Check power of 2
    temp = num
    while temp % 2 == 0:
        temp //= 2
    if temp == 1:
        return f"{num} is a power of 2"
        
    # Check power of 3
    temp = num
    while temp % 3 == 0:
        temp //= 3
    if temp == 1:
        return f"{num} is a power of 3"
        
    return f"{num} is neither a power of 2 nor 3"

# Floor value of square root of a number
def floor_sqrt(num):
    if num < 0: return None
    if num == 0 or num == 1: return num
    
    lo, hi = 1, num
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid == num:
            return mid
        elif mid * mid < num:
            lo = mid + 1
            ans = mid
        else:
            hi = mid - 1
    return ans

# Value of x to the power n using iteration
def power_iterative(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

# Value of x to the power n using recursion
def power_recursive(x, n):
    if n == 0:
        return 1
    return x * power_recursive(x, n - 1)


# =====================================================================
# WEEK 5 ASSIGNMENT: STACK AND LIST OPERATIONS (Functional Style)
# =====================================================================

# --- Stack Operations ---
def push(stack, item):
    stack.append(item)
    print(f"Pushed: {item}")

def pop(stack):
    if is_empty(stack):
        return "Stack is empty"
    return stack.pop()

def peek(stack):
    if is_empty(stack):
        return "Stack is empty"
    return stack[-1]

def is_empty(stack):
    return len(stack) == 0

# --- Delimiter Validation ---
def is_balanced(expression):
    stack = []
    open_delimiters = ["[", "{", "("]
    close_delimiters = ["]", "}", ")"]

    for char in expression:
        if char in open_delimiters:
            stack.append(char)
        elif char in close_delimiters:
            idx = close_delimiters.index(char)
            matching_open = open_delimiters[idx]
            
            if len(stack) == 0 or stack[-1] != matching_open:
                return False
            del stack[-1] # Remove item safely without built-in pop()
            
    return len(stack) == 0

# --- Count of elements in a list ---
def count_elements(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
            item_count = lst.count(item)
            print(f"{item} occurs {item_count} time(s)")

# --- Common elements from two lists ---
def find_common(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

# --- Making the list smaller by deleting recurring elements ---
def remove_recurring(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list


# =====================================================================
# EXECUTION & TEST CASES
# =====================================================================
if __name__ == "__main__":
    
    print("=== RUNNING WEEK 2 ASSIGNMENT ===")
    run_week_2_assignment()
    
    print("\n=== RUNNING WEEK 3 ASSIGNMENT ===")
    # Fibonacci Timing Test
    n_fib = 30
    start = time.perf_counter()
    res_iter = fibonacci_iterative(n_fib)
    time_iter = time.perf_counter() - start
    
    start = time.perf_counter()
    res_recur = fibonacci_recursive(n_fib)
    time_recur = time.perf_counter() - start
    
    print(f"Iterative Fib({n_fib}): {res_iter} (Took {time_iter:.6f}s)")
    print(f"Recursive Fib({n_fib}): {res_recur} (Took {time_recur:.6f}s)")
    
    print("Fibonacci series till 7th sequence:", fibonacci_series_sequence(7))
    print("Fibonacci series till value 50:", fibonacci_series_value(50))
    print("Is 3257 a Nice Number?", is_nice_number(3257))  # Ones=7(O), Tens=5(O)->False
    print("Is 2481 a Nice Number?", is_nice_number(2481))  # Ones=1(O), Tens=8(E), Hund=4(E)->False
    print("Is 345 a Nice Number?", is_nice_number(345))    # Ones=5(O), Tens=4(E), Hund=3(O)->True
    print(check_power_of_2_or_3(16))
    print(check_power_of_2_or_3(27))
    print("Floor sqrt of 20:", floor_sqrt(20))
    print("Power (Iterative) 5^3:", power_iterative(5, 3))
    print("Power (Recursive) 5^3:", power_recursive(5, 3))
    
    print("\n=== RUNNING WEEK 4 ASSIGNMENT ===")
    my_stack = []
    push(my_stack, 10)
    push(my_stack, 20)
    print("Peek Top:", peek(my_stack))
    print("Popped:", pop(my_stack))
    
    expr1 = "{[()() ]}"
    expr2 = "{[(])}"
    print(f"Is '{expr1}' balanced?", is_balanced(expr1))
    print(f"Is '{expr2}' balanced?", is_balanced(expr2))
    
    print("Counting list element occurrences:")
    count_elements([3, 7, 8, 3, 3, 7])
    
    list_a = [1, 2, 3, 4, 5, 3]
    list_b = [3, 4, 5, 6, 7, 3]
    print("Common elements:", find_common(list_a, list_b))
    
    dup_list = [1, 1, 2, 3, 8, 8, 6, 4, 4]
    print("Cleaned smaller list:", remove_recurring(dup_list))
