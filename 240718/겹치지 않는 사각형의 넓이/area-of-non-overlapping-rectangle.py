Ax1,Ay1,Ax2,Ay2=tuple(map(int,input().split()))
Bx1,By1,Bx2,By2=tuple(map(int,input().split()))
Mx1,My1,Mx2,My2=tuple(map(int,input().split()))
L=[[0 for _ in range(2000)]for _ in range(2000)]
offset=1000
Ax1,Ay1,Ax2,Ay2=Ax1+offset,Ay1+offset,Ax2+offset,Ay2+offset
Bx1,By1,Bx2,By2=Bx1+offset,By1+offset,Bx2+offset,By2+offset
Mx1,My1,Mx2,My2=Mx1+offset,My1+offset,Mx2+offset,My2+offset
for i in range(Ax1,Ax2):
    for j in range(Ay1,Ay2):
        L[i][j]=1
for i in range(Bx1,Bx2):
    for j in range(By1,By2):
        L[i][j]=1
for i in range(Mx1,Mx2):
    for j in range(My1,My2):
        L[i][j]=2
cnt=0
for row in L:
    for ele in row:
        if ele==1:
            cnt+=1
print(cnt)