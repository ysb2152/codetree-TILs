L=list(map(int,input().split()))
L1=L[::2]
L2=L[1::2]
if sum(L1)<sum(L2):
    print(sum(L2)-sum(L1))
elif sum(L1)>sum(L2):
    print(sum(L1)-sum(L2))
else:
    print("0")