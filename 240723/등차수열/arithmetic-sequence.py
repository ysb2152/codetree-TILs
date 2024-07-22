n=int(input())
L=list(map(int,input().split()))
L.sort()
max_comb=-999999
cnt=0
for k in range(10):
    
    for i in range(n):
        for j in range(i+1,n):
            if abs(L[i]-k)==abs(L[j]-k):
                cnt+=1
    max_comb=max(max_comb,cnt)
print(cnt)