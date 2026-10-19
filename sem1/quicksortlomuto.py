import time
import random
s=time.perf_counter()
def partition(arr,lo,hi):
    p=arr[hi]
    print(p)
    i=lo
    for j in range(lo,hi):
        if arr[j]<=p:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            print(arr)  
    print(arr[hi])
    arr[i],arr[hi]=arr[hi],arr[i]
    print(arr)
    return i
def quicksort(arr,lo,hi):
    if lo>hi:
     return
    p=partition(arr,lo,hi)
    quicksort(arr,lo,p-1)
    quicksort(arr,p+1,hi)
ar=[]
for i in range(100):
    ar.append(random.randint(1,100))
quicksort(ar,0,len(ar)-1)
print(ar)
e=time.perf_counter()
print(e-s)