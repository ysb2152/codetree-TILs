import sys

n=int(input())
L=[]
for _ in range(n):
    a=list(map(int,input().split()))
    L.append(a)
cnt=0
for i in range(n):
    for j in range(n-2):
        cnt=max(cnt,L[i][j]+L[i][j+1]+L[i][j+2])
print(cnt)