n,k=map(int,input().split())
L=[0 for _ in range(10000)]
offset=5000
maxi=0

for _ in range(n):
    candy,point=map(int,input().split())
    if L[point+offset]!=0:
        L[point+offset]+=candy
        continue
    L[point+offset]=candy

for c in range(len(L)):
    if c-k<0 or c+k>10000:
        continue
    cnt=0
    L1=L[c-k+1:c+k+2]
    for ele in L1:
        cnt+=ele
    
    
    maxi=max(maxi,cnt)

print(maxi)