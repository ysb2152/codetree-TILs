n=int(input())
L=list(map(int,input().split()))
k=[]
k=L[L.index(min(L)):]
print(f"{max(k)-min(k)}")