n,s=map(int,input().split())
L=list(map(int,input().split()))
L1=[]
L2=[]
for i in range(len(L)):
    L1.append(L[:i]+L[i+1:])
for i in range(len(L1)):
    for j in range(len(L1[1])):
        L2.append(L1[i][:j]+L1[i][j+1:])

for i in range(len(L2)):
    cnt=0
    for j in range(n-2):
        cnt+=L2[i][j]
    L2[i]=cnt

for i in range(len(L2)):
    L2[i]=abs(L2[i]-s)
print(min(L2))