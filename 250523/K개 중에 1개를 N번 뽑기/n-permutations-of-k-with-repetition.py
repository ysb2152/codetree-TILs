from itertools import product
k,n=map(int,input().split())
arr=[i for i in range(1,k+1)]
#print(arr)
a=list(product(arr,repeat=2))
for ele in a:
    for i in range(len(ele)):
        print(ele[i],end=" ")
    print(" ")