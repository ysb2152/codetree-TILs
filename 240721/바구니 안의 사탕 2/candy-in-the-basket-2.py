n,k=map(int,input().split())
L=[0 for _ in range(10000)]
offset=5000
maxi=0

for _ in range(n):
    candy,point=map(int,input().split())
    if L[point+offset]!=0:
        L[point+offset]+=candy
    L[point+offset]=candy

for c in range(len(L)):
    cnt=0
    L1=L[c-k:c+k+1]
    for ele in L1:
        if ele!=0:
            cnt+=ele
    
    
    maxi=max(maxi,cnt)
print(maxi)