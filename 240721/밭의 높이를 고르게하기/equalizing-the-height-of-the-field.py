n,h,t=map(int,input().split())
L=list(map(int,input().split()))
min_cnt=9999
for i in range(0,n-t+1):
    cnt=0
    for j in range(i,i+t):
        
        cnt+=abs(L[j]-h)
    
    min_cnt=min(min_cnt,cnt)
print(min_cnt)