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
    
    r,c=start[i]
    count[r][c]=1
#for row in count:
    #print(row)
#print(" ")
for _ in range(t):
    new_count=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            
            if count[i][j]==1:
                prev_r,prev_c=i,j
                for dx,dy in zip(dxs,dys):
                    new_r,new_c=i+dx,j+dy
                    if in_range(new_r,new_c) and L[new_r][new_c]>=L[prev_r][prev_c]:
                        if L[prev_r][prev_c]==L[new_r][new_c]:
                            continue
                        else:
                               
                            prev_r,prev_c=new_r,new_c
                    
                new_count[prev_r][prev_c]+=1
    #for row in new_count:
        #print(row)
    #print(" ")
    for k in range(n):
        for l in range(n):
            if new_count[k][l]>1:
                new_count[k][l]=0
    #for row in new_count:
        #print(row)
    #print(" ")
    count=new_count
cnt=0
for row in count:
    for ele in row:
        if ele==1:
            cnt+=1
print(cnt)