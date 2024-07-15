n=int(input())
L=list(map(int,input().split()))
L.sort()
for ele in L:
    print(ele,end=" ")
L.sort(reverse=True)
print(" ")
for ele in L:
    print(ele,end=" ")