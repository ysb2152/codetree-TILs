n,k=map(int,input().split())
L=[0 for _ in range(10000)]
for _ in range(n):
    pos,alpha=input().split()
    pos=int(pos)-1
    if alpha=='G':
        alpha=1
    if alpha=='H':
        alpha=2
    L[pos]=alpha
max_cnt=0
for i in range(10000-k):
    cnt=0
    for j in range(i,i+k+1):
        cnt+=L[j]
    max_cnt=max(max_cnt,cnt)
print(max_cnt)