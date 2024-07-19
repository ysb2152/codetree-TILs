n=int(input())
L=[]
for _ in range(n):
    a,b=tuple(input().split())
    L.append([int(a),int(b)])
possi=[]
for i in range(1,n-1):
    possi.append(L[:i]+L[i+1:])
dis=0
min_dis=0
mini=[]

if n==3:
    dis+=abs(possi[0][0][0]-possi[0][1][0])
    dis+=abs(possi[0][0][1]-possi[0][1][1])
    mini.append(dis)
if n==4:
    for i in range(len(possi)):
        for j in range(1,len(possi[i])-1):
            dis=0
        
            dis+=abs(possi[i][0][0]-possi[i][1][0])
            dis+=abs(possi[i][0][1]-possi[i][1][1])
                
            for k in range(0,2):
                dis+=abs(possi[i][j][k]-possi[i][j+1][k])
            mini.append(dis)
        
    
else:
    for i in range(len(possi)):
        for j in range(1,len(possi[i])-1):
            dis=0
        
            dis+=abs(possi[i][0][0]-possi[i][1][0])
            dis+=abs(possi[i][0][1]-possi[i][1][1])
            dis+=abs(possi[i][n-3][0]-possi[i][n-2][0])
            dis+=abs(possi[i][n-3][1]-possi[i][n-2][1])
        
            for k in range(0,2):
                dis+=abs(possi[i][j][k]-possi[i][j+1][k])
            mini.append(dis)
print(min(mini))