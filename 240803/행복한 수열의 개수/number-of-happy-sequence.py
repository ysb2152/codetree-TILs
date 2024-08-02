n,m=map(int,input().split())
L=[list(map(int,input().split()))for _ in range(n)]
def in_range(a,b):
    return 0<=a and a<n and 0<=b and b<n
cnt=0

for i in range(n):
    for j in range(n-m+1):
        if L[i][j:j+m].count(L[i][j])==m:
            
            cnt+=1
            break
ReversedL=[]
for i in range(n):
    c=[]
    for j in range(n):
        c.append(L[j][i])
    ReversedL.append(c)

for i in range(n):
    for j in range(n-m+1):
        if ReversedL[i][j:j+m].count(ReversedL[i][j])==m:
            
            cnt+=1
            break
print(cnt)