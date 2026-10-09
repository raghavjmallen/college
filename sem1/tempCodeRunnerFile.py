ar=[]
for i in range(10):
    ar.append(random.randint(1,100))
quicksort(ar,0,len(ar)-1)
print(ar)
e=time.perf_counter()
print(e-s)