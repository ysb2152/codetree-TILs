n=int(input())
L=[0 for _ in range(n+1)]
L[1]=2
def comp(a):
    if a==1:
        return 2
    else:
        return comp(int(a/2))+comp(a-1)
for i in range(1,n+1):
    print(comp(i),end=" ")
