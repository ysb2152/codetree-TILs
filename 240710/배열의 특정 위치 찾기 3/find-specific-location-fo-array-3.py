L=list(map(int,input().split()))
summ=0
L2=[]
for i in range(0,len(L)):
    if L[i]==0:
        L2=L[i-3:i]
        break
for ele in L2:
    summ+=ele

print(summ)