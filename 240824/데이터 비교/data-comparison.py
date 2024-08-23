n=int(input())
L1=list(map(int,input().split()))
L1=set(L1)
m=int(input())
L2=list(map(int,input().split()))

for ele in L2:
    if ele not in L1:
        print("0",end=" ")
    else:
        print("1",end=" ")