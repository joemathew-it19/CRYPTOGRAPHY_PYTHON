No_it=int(input())
r1,r2=map(int,input().split())
Target=int(input())
l1,l2=[],[]
cost,final=0,0
l=[31,28,31,30,31,30,31,31,30,31,30,31]
for j in range(len(l)):
    for k in range(1,l[j]+1):
        l1.append((6-(j+1))**2+abs(k-15))
    l2.append(l1)
    l1=[]
for i in range(No_it+1):
    for j in l2:
        for k in j:
            if(k>=No_it):
                t=No_it-i
                cost=cost+(i*r1+t*r2)
            else:
                h=No_it-i
                t=k-h
                if(t<=0):
                    cost=cost+(k*r2)
                else:
                    cost=cost+(t*r1+h*r2)
        final=final+cost
        cost=0
    if(final>=Target):
        print(i)
        break
    else:
        final=0
else:
    print(No_it)
        
        
    
