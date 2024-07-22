n=int(input())
L=[tuple(map(int,input().split()))for _ in range(n)]
min_max=99999
for i in range(0,101,2):
    
    for j in range(0,101,2):
        mimi=0
        plmi=0
        mipl=0
        plpl=0
        for k in range(n):
            a,b=L[k]
            if a<i and b<j:
                mimi+=1
                continue
            if a>i and b<j:
                plmi+=1
                continue
            if a<i and b>j:
                mipl+=1
                continue
            if a>i and b>i:
                plpl+=1
                continue
        
        maxi=max(mimi,plmi,mipl,plpl)
        
        min_max=min(min_max,maxi)
print(min_max)