n,m=map(int,input().split())
L=[list(map(int,input().split()))for _ in range(n)]
max_sum=-99999
for i in range(n):
    for j in range(m-2):
        max_sum=max(max_sum,sum(L[i][j:j+3]))
ReversedL=[]
for i in range(m):
    c=[]
    for j in range(n):
        c.append(L[j][i])
    ReversedL.append(c)
for i in range(m):
    for j in range(n-2):
        max_sum=max(max_sum,sum(ReversedL[i][j:j+3]))
for i in range(n):
    if i==n-1:
        continue
    for j in range(m-1):
        cnt1=L[i][j]+L[i][j+1]+L[i+1][j]
        cnt2=L[i][j]+L[i][j+1]+L[i+1][j+1]
        max_sum=max(max_sum,cnt1)
        max_sum=max(max_sum,cnt2)

for i in range(m):
    if i==m-1:
        continue
    for j in range(n-1):
        cnt1=ReversedL[i][j]+ReversedL[i][j+1]+ReversedL[i+1][j]
        cnt2=ReversedL[i][j]+ReversedL[i][j+1]+ReversedL[i+1][j+1]
        max_sum=max(max_sum,cnt1)
        max_sum=max(max_sum,cnt2)
print(max_sum)