L=list(map(int,input().split()))
s=0
leng=len(L)
for ele in L:
    if ele>=250:
        L=L[:L.index(ele)]
        break
    s+=ele


   
print(s,end=" ")
print(f"{(s/(len(L))):.1f}")