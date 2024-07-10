n=int(input())
L=[]
L.append(1)
L.append(n)
for i in range(2,100):
    
    L.append(L[i-2]+L[i-1])
    if (L[i-2]+L[i-1])>=100:
        break
for ele in L:
    print(ele,end=" ")