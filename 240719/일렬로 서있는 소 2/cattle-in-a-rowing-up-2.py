import sys
n=int(input())
L=list(map(int,input().split()))
a=[]
cnt=0
for i in range(len(L)):
    for j in range(i+1,len(L)):
        for k in range(j+1,len(L)):
            a.append([i,j,k])
for row in a:
    if L[row[0]]<=L[row[1]]<=L[row[2]]:
        cnt+=1
print(cnt)