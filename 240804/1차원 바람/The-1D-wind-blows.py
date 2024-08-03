n,m,q=map(int,input().split())
L=[list(map(int,input().split()))for _ in range(n)]
def in_range(a):
    return 0<=a<n
def shift(a,d):
    if d=='L':
        temp=L[a][m-1]
        for i in range(m-1,0,-1):
            L[a][i]=L[a][i-1]
        L[a][0]=temp
        d='R'
    else:
        temp=L[a][0]
        for i in range(m-1):
            L[a][i]=L[a][i+1]
        L[a][m-1]=temp
        d='L'
    return L,d
def upcheck(r):
    check=False
    for i in range(m):
        if in_range(r-1) and L[r-1][i]==L[r][i]:
            check=True
    r=r-1
    return check
def downcheck(r):
    check=False
    for i in range(m):
        if in_range(r+1) and L[r+1][i]==L[r][i]:
            check=True
    r=r+1
    return check

for _ in range(q):
    r,d=input().split()
    r=int(r)-1
    L,d=shift(r,d)
    up,upd=r,d
    down,downd=r,d
    while True:
        if upcheck(up):
            up-=1
            L,upd=shift(up,upd)
        else:
            break
    while True:
        if downcheck(down):
            down+=1
            
            L,downd=shift(down,downd)
            
            
        else:
            break




for row in L:
    for ele in row:
        print(ele,end=" ")
    print(" ")