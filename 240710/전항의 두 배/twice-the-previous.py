a,b=map(int,input().split())
L=[a,b]

for i in range(2,10):
    L.append(L[i-1]+2*L[i-2])
for ele in L:
    print(ele,end=" ")