L=list(map(int,input().split()))
def summ(a,b,c):
    sum1=L[a]+L[b]+L[c]
    sum2=sum(L)-sum1
    return abs(sum1-sum2)
mini=200
for i in range(0,6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            mini=min(mini,summ(i,j,k))
print(mini)