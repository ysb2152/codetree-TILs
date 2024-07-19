import sys

n=int(input())
L=list(map(int,input().split()))
min_val=sys.maxsize

for i in range(len(L)):
    sum_diff=0
    for j in range(len(L)):
        
        sum_diff+=L[j]*abs(i-j)
        
    
    min_val=min(min_val,sum_diff)
print(min_val)