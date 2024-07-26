n=int(input())
L=list(map(int,input().split()))
t=min(L)
s=[]
for i in range(n):
    s.append(L[i])

for i in range(n):
    if t in s:
        s.remove(t)

if s==[]:
    print("-1")
elif min(s) in L:
    p=L.index(min(s))+1
    L.remove(min(s))
    if min(s) in L:
        print("-1")
    else:
        print(p)
else:
    print("-1")