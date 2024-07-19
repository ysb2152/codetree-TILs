a=(input())
L=[int(c) for c in a]
t=[int(c) for c in a]
p=[]
maxx=0
for i in range(1,len(L)):
    t=[int(c) for c in a]
    if L[i]==1:
        t[i]=0
        p.append(t)
        continue
    if L[i]==0:
        t[i]=1
        p.append(t)
        continue

for row in p:
    cnt=0
    for ele in row:
        cnt=cnt*2+ele
    maxx=max(maxx,cnt)
print(maxx)