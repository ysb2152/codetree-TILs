n,q=map(int,input().split())
L=list(map(int,input().split()))
for _ in range(q):
    k=list(map(int,input().split()))
    if k[0]==1:
        print(L[k[1]-1])
    if k[0]==2:
        for i in L:
            if i==k[1]:
                print(L.index(i)+1)
                break
            elif L.index(i)==k[1]:
                print("0")
    if k[0]==3:
        for i in range(k[1],k[2]+1):
            if i==k[2]:
                print(L[i-1])
                break
            print(L[i-1],end=" ")