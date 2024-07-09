L=list(map(int,input().split()))

for ele in L:
    if ele%3==0:
        print(L[L.index(ele)-1])
        break