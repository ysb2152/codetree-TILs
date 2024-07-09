L=list(map(int,input().split()))
L1=L[1::2]
L2=[]
for i in range(1,len(L)+1):
    if i%3==0:
        L2.append(i)

print(sum(L1),end=" ")
print(f"{(sum(L2)/len(L2)):.1f}")