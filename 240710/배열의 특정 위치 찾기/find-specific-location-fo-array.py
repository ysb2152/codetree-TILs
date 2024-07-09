L=list(map(int,input().split()))
L1=L[1::2]
L2=L[2::3]


print(sum(L1),end=" ")
print(f"{(sum(L2)/len(L2)):.1f}")