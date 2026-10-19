def weighed_total(mid,final):
    n=[]
    Mid=[]
    for name,marks in mid.items():
        n.append(name)
        Mid.append(marks)
    Final=[0]
    for name,marks in final.items():
        i=0
        while i!=-1:
            if name==n[i]:
                Final[i]=marks
                i=-1
            else:
                Final.append([])
                i+=1
    w=[]
    for j in range(0,len(n)):
        w.append(((Mid[j]/30)*0.4+(Final[j]/60)*0.6)*100)
    dict={}
    for j in range(0,len(n)):
        dict[n[j]]=w[j]
    for a,b in dict.items():
        print(a,b)
mid={"a":21,"b":25,"c":19}
final={"b":50,"c":45,"a":60}
weighed_total(mid,final)
        


        
