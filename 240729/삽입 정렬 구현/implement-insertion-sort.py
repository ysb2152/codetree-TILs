n=int(input())
L=list(map(int,input().split()))
for i in range(1,len(L)):
    j=i-1
    key=L[i]
    while j>=0 and L[j]>key:
        L[j+1]=L[j]
        j-=1
    L[j+1]=key
for ele in L:
    print(ele,end=" ")