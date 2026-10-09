def siftdown(a,i,heapsize):
    while True:
        largest=i
        left =2*i+1
        right=2*i+2
        if left< heapsize and a[left] >a[largest]:
            largest=left
        if right<heapsize and a[right]>a[largest]:
            largest=right
        if largest==i:
            return 
        a[i],a[largest]=a[largest],a[i]
        i=largest
def buildmaxheap(a,n):
    firstleaf=(n-1)//2
    lastinternal=firstleaf-1
    for i in range(lastinternal,-1,-1):
        siftdown(a,i,n)
ar=[2,6,8,4,9,3,1,0,7,5,10]
buildmaxheap(ar,len(ar))
print(ar)

        