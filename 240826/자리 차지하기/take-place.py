from sortedcontainers import SortedSet
ss=SortedSet()
n,m=map(int,input().split())
L=list(map(int,input().split()))
seats=[0 for _ in range(m)]
cnt=0
for i in range(len(L)):
    ss.add(L[i]-1)

for i in range(len(ss)-1,-1,-1):
    if seats[ss[i]]!=0:
        break
    else:
        cnt+=1
print(cnt)