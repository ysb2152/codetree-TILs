n=int(input())
L=[tuple(map(int,input().split()))for _ in range(n)]
cnt=0
S=[]
        
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            cou=[0 for _ in range(1000)]
            cov=0
            for p in range(n):
                if p==i or p==j or p==k:
                    continue
                start,end=L[p]
                for l in range(start,end+1):
                    cou[l]+=1
            S.append(cou)
                
for row in S:
    cord=0
    for ele in row:
        
        if ele==0:
            cord+=1
        if ele==1:
            cord+=1
    if cord==len(row):
        cnt+=1
print(cnt)