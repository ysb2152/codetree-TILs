n=int(input())
a,b,c=map(int,input().split())
nopen=[]
for i in range(1,n+1):
    if abs(a-i)<=2:
        continue
    for j in range(1,n+1):
        if abs(b-j)<=2:
            continue
        for k in range(1,n+1):
            if abs(c-k)<=2:
                continue
            nopen.append([i,j,k])
print((n*n*n)-len(nopen))