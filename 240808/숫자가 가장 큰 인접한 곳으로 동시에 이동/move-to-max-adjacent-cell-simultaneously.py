n,m,t=map(int,input().split())
L=[list(map(int,input().split()))for _ in range(n)]
start=[]
dxs,dys=[-1,1,0,0],[0,0,-1,1]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
for _ in range(m):
    r,c=map(int,input().split())
    r-=1
    c-=1
    start.append((r,c))
count=[[0 for _ in range(n)]for _ in range(n)]

for i in range(m):
    new_count=[[0 for _ in range(n)]for _ in range(n)]
    r,c=start[i]
    count[r][c]=1
#for row in count:
    #print(row)
#print(" ")
for _ in range(t):
    
    for i in range(n):
        for j in range(n):
            s=[]
            if count[i][j]==1:
                for dx,dy in zip(dxs,dys):
                    new_r,new_c=i+dx,j+dy
                    if in_range(new_r,new_c):
                        s.append([new_r,new_c,L[new_r][new_c]])
                s.sort(key=lambda x: x[2],reverse=True)
                new_count[s[0][0]][s[0][1]]+=1
    #for row in new_count:
        #print(row)
    for k in range(n):
        for l in range(n):
            if new_count[k][l]>1:
                new_count[k][l]=0
    count=new_count
cnt=0
for row in count:
    for ele in row:
        if ele==1:
            cnt+=1
print(cnt)