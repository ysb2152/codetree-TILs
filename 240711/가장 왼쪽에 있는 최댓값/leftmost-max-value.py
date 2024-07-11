n=int(input())
L=list(map(int,input().split()))
while L!=[]:
    
    print(f"{L.index(max(L))+1}",end=" ")
    L=L[:L.index(max(L))]