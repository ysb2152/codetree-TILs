n=int(input())
L=list(map(int,input().split()))
L.sort()
min_diff=9999

for i in range(1,n):
        
    cnt=abs(L[i]-L[i+n])
    
    min_diff=min(min_diff,cnt) 

print(min_diff)