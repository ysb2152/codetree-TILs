n,m,k=map(int,input().split())
L=[0 for _ in range(n)]
p=[]
for i in range(m):
    a=int(input())
    L[a-1]+=1
    for i in range(n):
        if L[i]>=k:
            p.append(i+1)
if p!=[]:
    print(p[0])
else:
    print("-1")