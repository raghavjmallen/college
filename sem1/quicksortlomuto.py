import time
import random
s=time.perf_counter()
def partition(arr,lo,hi):
    p=arr[hi]
    print(p)
    i=lo-1
    for j in range(lo,hi):
        if arr[j]<=p:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            print(arr)  
    print(arr[hi])
    arr[i+1],arr[hi]=arr[hi],arr[i+1]
    print(arr)
    return i+1
def quicksort(arr,lo,hi):
    if lo<hi:
        p=partition(arr,lo,hi)
        quicksort(arr,lo,p-1)
        quicksort(arr,p+1,hi)
ar=[]
for i in range(1000):
    ar.append(random.randint(1,100))
quicksort(ar,0,len(ar)-1)
print(ar)
e=time.perf_counter()
print(e-s)