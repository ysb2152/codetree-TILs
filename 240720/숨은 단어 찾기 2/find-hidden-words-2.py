n,m=map(int,input().split())
L=[list(input()) for _ in range(n)]
def in_range(a,b):
    return 0<=a and a<n and 0<=b and b<m
cnt=0
for i in range(n):
    for j in range(m):
        if in_range(i,j) and in_range(i,j+1) and in_range(i,j+2) and L[i][j]=='L' and L[i][j+1]=='E' and L[i][j+2]=='E':
            cnt+=1
        if in_range(i,j-1) and in_range(i,j-2) and L[i][j]+L[i][j-1]+L[i][j-2]=='LEE':
            cnt+=1
        if in_range(i-1,j) and in_range(i-2,j) and L[i][j]+L[i-1][j]+L[i-2][j]=='LEE':
            cnt+=1
        if in_range(i+1,j) and in_range(i+2,j)  and L[i][j]+L[i+1][j]+L[i+2][j]=='LEE':
            cnt+=1
        if in_range(i+1,j+1) and in_range(i+2,j+2) and L[i][j]+L[i+1][j+1]+L[i+2][j+2]=='LEE':
            cnt+=1
        if in_range(i-1,j-1) and in_range(i-2,j-2) and L[i][j]+L[i-1][j-1]+L[i-2][j-2]=='LEE':
            cnt+=1 
        if in_range(i-1,j+1) and in_range(i-2,j+2) and L[i][j]+L[i-1][j+1]+L[i-2][j+2]=='LEE':
            cnt+=1 
        if in_range(i+1,j-1) and in_range(i+2,j-2) and L[i][j]+L[i+1][j-1]+L[i+2][j-2]=='LEE':
            cnt+=1 
print(cnt)