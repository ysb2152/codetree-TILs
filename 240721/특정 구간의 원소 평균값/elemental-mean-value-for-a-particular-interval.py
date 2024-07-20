n=int(input())
L=list(map(int,input().split()))
cnt=0
for i in range(n):
    for j in range(i,n):
        sum_val=0
        
        for k in range(i,j+1):
            if i==j:
                sum_val+=L[i]*2
                continue
            sum_val+=L[k]
        if i==j:
            sum_val/=2
            cnt+=1
            continue
        
        sum_val/=(j-i+1)
        
        if sum_val in L[i:j+1]:
            cnt+=1
print(cnt)