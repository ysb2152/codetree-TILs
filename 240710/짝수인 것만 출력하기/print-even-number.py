n=int(input())
L=list(map(int,input().split()))
k=[]
for ele in L:
    if ele%2==0:
        k.append(ele)
for ele in k:
    print(f"{ele}",end=" ")