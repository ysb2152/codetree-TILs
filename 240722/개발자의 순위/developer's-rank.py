k,n=map(int,input().split())
L=[list(map(int,input().split()))for _ in range(k)]
R1=[]
R2=[]
R3=[]
cnt=0
for i in range(n):
    for j in range(i+1,n):
        R1.append([L[0][i],L[0][j]])
for i in range(n):
    for j in range(i+1,n):
        R2.append([L[1][i],L[1][j]])
for i in range(n):
    for j in range(i+1,n):
        R3.append([L[2][i],L[2][j]])
for i in range(len(R1)):
    if (R1[i] in R2) and (R1[i] in R3):
        cnt+=1
print(cnt)