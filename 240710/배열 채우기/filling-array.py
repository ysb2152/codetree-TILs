L=list(map(int,input().split()))
L1=[]
for ele in L:
    if ele==0:
        L1=L1[::-1]
        break
    L1.append(ele)
for ele in L1:
    print(ele,end=" ")