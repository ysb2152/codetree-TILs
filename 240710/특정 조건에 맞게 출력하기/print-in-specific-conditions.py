L=list(map(int,input().split()))
for ele in L:
    if ele==0:
        break
    elif ele%2==1:
        print(f"{ele+3}",end=" ")
    elif ele%2==0:
        print(f"{ele//2}",end=" ")