n=int(input())
L=list(map(int,input().split()))
min_sum=99999
for i in range(n):
    L[i]*=2

    for j in range(n):
        comb=[]
        summ=0
        for k in range(n):
            if k!=j:
                comb.append(L[k])
        

        
        for k in range(n-2):
            summ+=abs(comb[k+1]-comb[k])
        
        

        min_sum=min(min_sum,summ)
    L[i]//=2
print(min_sum)