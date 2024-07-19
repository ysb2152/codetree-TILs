n=int(input())
L=[]
for _ in range(n):
    p=int(input())
    L.append(p)
leng=[]
mini=[]
cnt=0
for i in range(len(L)):
    leng.append(L[i:]+L[:i])

for i in range(len(leng)):
    cnt=0
    for j in range(n):
        cnt+=leng[i][j]*(j)
       
    mini.append(cnt)
print(min(mini))