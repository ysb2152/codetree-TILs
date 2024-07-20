n=int(input())
a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())
nopen=[]
for i in range(1,n+1):
    if abs(i-a1)<=2 or (i==n and a1+i<=n+2) or (i==n-1 and a1+i==n) or ((i==1 or i==2) and a1==n) or ((i==1) and a1==n-1):
        continue
    for j in range(1,n+1):
        if abs(j-b1)<=2 or (j==n and b1+j<=n+2) or (j==n-1 and b1+j==n) or ((j==1 or j==2) and b1==n) or ((j==1) and b1==n-1):
            continue
        for k in range(1,n+1):
            if abs(k-c1)<=2or (k==n and c1+k<=n+2) or (k==n-1 and c1+k==n) or ((k==1 or k==2) and c1==n) or ((k==1) and c1==n-1):
                continue
            nopen.append([i,j,k])
for i in range(1,n+1):
    if abs(i-a2)<=2 or (i==n and a2+i<=n+2) or (i==n-1 and a2+i==n) or ((i==1 or i==2) and a2==n) or ((i==1) and a2==n-1):
        continue
    for j in range(1,n+1):
        if abs(j-b2)<=2 or (j==n and b2+j<=n+2) or (j==n-1 and b2+j==n) or ((j==1 or j==2) and b2==n) or ((j==1) and b2==n-1):
            continue
        for k in range(1,n+1):
            if abs(k-c2)<=2or (k==n and c2+k<=n+2) or (k==n-1 and c2+k==n) or ((k==1 or k==2) and c2==n) or ((k==1) and c2==n-1):
                continue
            nopen.append([i,j,k])
print(len(nopen)-1)