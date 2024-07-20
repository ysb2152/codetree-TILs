n=int(input())
L=list(map(int,input().split()))
cnt=0
for i in range(n):
    for j in range(i,n):
        sum_val=0
        for k in range(i,j+1):
            sum_val+=L[k]
        sum_val//=(j+1)
        if sum_val in L[i:j+1]:
            cnt+=1
print(cnt)