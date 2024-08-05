n=int(input())
L=[]
for _ in range(n):
    a=int(input())
    L.append(a)
s1,e1=map(int,input().split())
s2,e2=map(int,input().split())
s1,e1,s2,e2=s1-1,e1-1,s2-1,e2-1
ans=[]
ans2=[]
for i in range(n):
    if i>=s1 and i<=e1:
        continue
    ans.append(L[i])
for i in range(len(ans)):
    if i>=s2 and i<=e2:
        continue
    ans2.append(ans[i])
if len(ans2)==0:
    print("0")
else:
    print(len(ans2))
    for ele in ans2:
        print(ele)