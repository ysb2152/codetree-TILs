n=int(input())
L=list(map(int,input().split()))
L.sort()
max_comb=0

for k in range(1,101):
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if (L[i]+L[j])/2==k:
                cnt+=1
    max_comb=max(max_comb,cnt)
print(max_comb)