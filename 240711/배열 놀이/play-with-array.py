n,q=map(int,input().split())
L=list(map(int,input().split()))
for _ in range(q):
    k=list(map(int,input().split()))
    if k[0]==1:
        print(L[k[1]-1])
    if k[0]==2:
        for i in range(0,n):
            if L[i]==k[1]:
                print(i+1)
                break
            if i==n-1:
                print("0")
                break
                
    if k[0]==3:
        for i in range(k[1],k[2]+1):
            if i==k[2]:
                print(L[i-1])
                break
            print(L[i-1],end=" ")