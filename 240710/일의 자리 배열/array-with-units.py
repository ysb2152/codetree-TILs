a,b=map(int,input().split())
L=[]
L.append(a)
L.append(b)

for i in range(2,10):
    L.append(L[i-2]+L[i-1])
for ele in L:
    if ele//10>=1:
        ele=ele-(10*(ele//10))
    print(f"{ele}",end=" ")