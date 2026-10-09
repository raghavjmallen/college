import random
import time
s = time.perf_counter()
def hoare_partition(arr, lo, hi):
    pivot = arr[lo]
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
def hoare_quicksort(arr, lo, hi):
    if lo < hi:
        p = hoare_partition(arr, lo, hi)
        hoare_quicksort(arr, lo, p)
        hoare_quicksort(arr, p + 1, hi)
ar=[]
for i in range(1000):
    ar.append(random.randint(1,100))
hoare_quicksort(ar,0,len(ar)-1)
print(ar)
e=time.perf_counter()
print(e-s)
