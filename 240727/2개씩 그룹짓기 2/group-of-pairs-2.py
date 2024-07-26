n=int(input())
L=list(map(int,input().split()))
L.sort()
min_diff=9999
L=[0]+L
for i in range(1,n+1):
        
    
    min_diff=min(min_diff,L[i+n]-L[i]) 

print(min_diff)