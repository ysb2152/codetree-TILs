n=int(input())
L=list(map(int,input().split()))
for i in range(len(L)-1):
    minimum=i
    for j in range(i+1,len(L)):
        if L[j]<L[minimum]:
            minimum=j
    temp=L[i]
    L[i]=L[minimum]
    L[minimum]=temp
for ele in L:
    print(ele,end=" ")