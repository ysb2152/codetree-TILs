L=list(map(int,input().split()))
L1=[]
for ele in L:
    if ele==0:
        break
    
    L1.append(ele)
L1=L1[::-1]
for ele in L1:
    print(ele,end=" ")