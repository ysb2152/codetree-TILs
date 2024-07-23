n,m=map(int,input().split())
L=[tuple(map(int,input().split()))for _ in range(m)]
max_cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        cnt=0
        for a,b in L:
            if (a==i and b==j) or (b==i and a==j):
                cnt+=1
        max_cnt=max(max_cnt,cnt)
print(max_cnt)