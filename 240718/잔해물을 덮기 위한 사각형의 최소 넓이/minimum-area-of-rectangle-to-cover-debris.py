Ax1,Ay1,Ax2,Ay2=tuple(map(int,input().split()))
Bx1,By1,Bx2,By2=tuple(map(int,input().split()))
L=[[0 for _ in range(2000)]for _ in range(2000)]
offset=1000
Ax1,Ay1,Ax2,Ay2=Ax1+offset,Ay1+offset,Ax2+offset,Ay2+offset
Bx1,By1,Bx2,By2=Bx1+offset,By1+offset,Bx2+offset,By2+offset
for i in range(Ax1,Ax2):
    for j in range(Ay1,Ay2):
        L[i][j]=1
for i in range(Bx1,Bx2):
    for j in range(By1,By2):
        L[i][j]+=2
index=[]
jndex=[]
for i in range(2000):
    for j in range(2000):
        if L[i][j]==1:
            index.append(i)
            jndex.append(j)

print((max(index)-min(index)+1)*(max(jndex)-min(jndex)+1))