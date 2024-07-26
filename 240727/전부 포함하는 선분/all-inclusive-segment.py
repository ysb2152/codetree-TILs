n=int(input())
L=[tuple(map(int,input().split()))for _ in range(n)]
min_cnt=99999
for i in range(n):
    t1=[]
    t2=[]
    for j in range(n):
        if j==i:
            continue
        t1.append(L[j][0])
        t2.append(L[j][1])
    min_cnt=min(min_cnt,max(t2)-min(t1))
print(min_cnt)