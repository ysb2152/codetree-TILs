n,m=map(int,input().split())
L=[list(map(int,input().split()))for _ in range(n)]
c=[int(input())-1 for _ in range(m)]

dxs,dys=[1,0,-1,0],[0,1,0,-1]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def exp(c):
    
    for a in range(n):
        if L[a][c]==0:
            continue
            
        else:
            bomb=L[a][c]
            
            L[a][c]=0
            for dx,dy in zip(dxs,dys):
                for i in range(1,bomb):
                    if in_range(a+i*dx,c+i*dy):
                        L[a+i*dx][c+i*dy]=0
            
            break
        


for k in range(m):
    ans2=[[0 for _ in range(n)]for _ in range(n)]
    exp(c[k])
    
    
    for i in range(n):
        ans2_row=n-1
        for j in range(n-1,-1,-1):
            if L[j][i]!=0:
                ans2[ans2_row][i]=L[j][i]
            
                ans2_row-=1
            else:
                ans2[ans2_row][i]=0
    
    
    L=ans2
    


for row in ans2:
    for ele in row:
        print(ele,end=" ")
    print(" ")