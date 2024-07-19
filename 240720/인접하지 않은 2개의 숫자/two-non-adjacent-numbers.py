n=int(input())
L=list(map(int,input().split()))
p=[]
for i in range(n):
    if i==0:
        p.append(L[i+2:])
        continue
    if i==1:
        p.append(L[i+2:])
        continue
    if i==n-2:
        p.append(L[:i-1])
        continue

    if i==n-1:
        p.append(L[:i-1])
        continue
    p.append(L[:i-1]+L[i+2:])
for i in range(n):
    max_diff=0
    diff=0
    for j in range(len(p[i])):
        diff=(L[i])+p[i][j]
        max_diff=max(max_diff,diff)
print(max_diff)