n,m=map(int,input().split())
L=[list(map(int,input().split()))for _ in range(n)]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
dxs,dys=[-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]

for _ in range(m):
    for i in range(1,n*n+1):
        cnt=0
        new_L=[L[:]for L in L]
        maxs=[]
        for j in range(n):
            for k in range(n):
                
                if L[j][k]==i and cnt==0:
                    for dx,dy in zip(dxs,dys):
                        if in_range(j+dx,k+dy):
                            maxs.append([L[j+dx][k+dy],j+dx,k+dy])
                    maxs.sort(key=lambda x: x[0],reverse=True)
                    new_L[j][k]=maxs[0][0]
                    new_L[maxs[0][1]][maxs[0][2]]=i
                    L=new_L
                    cnt+=1
for row in L:
    for ele in row:
        print(ele,end=" ")
    print(" ")