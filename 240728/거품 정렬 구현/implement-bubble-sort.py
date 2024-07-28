n=int(input())
L=list(map(int,input().split()))
lenn=len(L)
for i in range(lenn):
    for j in range(lenn-1-i):
        if L[j]>L[j+1]:
            temp=L[j]
            L[j]=L[j+1]
            L[j+1]=temp
for ele in L:
    print(ele,end=" ")