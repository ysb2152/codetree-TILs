n,k=map(int,input().split())
L=[]
for _ in range(n):
    a=int(input())
    L.append(a)
L.sort()
max_can=-999
for i in range(n):
    cnt=0
    can=[]
    can.append(L[i])
    
    for j in range(i+1,n):
        can.append(L[j])
        if abs(min(can)-max(can))<=k:
            continue
        else:
            can.pop(len(can)-1)
            continue
    
    max_can=max(max_can,len(can))
print(max_can)