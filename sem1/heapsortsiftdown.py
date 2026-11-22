def siftdown(a, i, heapsize):
    while True:
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < heapsize and a[left] > a[largest]:
            largest = left
        if right < heapsize and a[right] > a[largest]:
            largest = right
        if largest == i:
            return
        a[i], a[largest] = a[largest], a[i]
        i = largest

def buildmaxheap(a, n):
    lastinternal = n//2 - 1          # fixed (see note below)
    for i in range(lastinternal, -1, -1):
        siftdown(a, i, n)

def heapsort(a, n):
    buildmaxheap(a, n)
    for end in range(n-1, 0, -1):
        a[0], a[end] = a[end], a[0]  # move current max to the end
        siftdown(a, 0, end)          # heap is now only a[0..end-1]

ar = [2, 6, 8, 4, 9, 3, 1, 0, 7, 5, 10]
buildmaxheap(ar, len(ar))
print("Max heap:", ar)
heapsort(ar, len(ar))
print("Sorted:  ", ar)