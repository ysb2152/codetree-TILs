k,n=map(int,input().split())
L=[list(map(int,input().split()))for _ in range(k)]
R1=[]
R2=[]
R3=[]
cnt=0
for l in range(k):
    for i in range(n):
        for j in range(i+1,n):
            R1.append([L[l][i],L[l][j]])
for row in R1:
    cnt=R1.count(row)
    
    if cnt==k:
        R2.append(row)
for row in R2:
    if row not in R3:
        R3.append(row)

            
           
    

print(len(R3))