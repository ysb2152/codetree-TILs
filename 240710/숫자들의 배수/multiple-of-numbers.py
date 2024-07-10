n=int(input())
cnt=0
L=[n*i for i in range(1,30)]
for ele in L:
    if cnt==2:
        break
    if ele%5==0:
        cnt+=1
    print(f"{ele}",end=" ")