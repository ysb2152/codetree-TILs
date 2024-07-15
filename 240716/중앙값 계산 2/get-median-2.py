n=int(input())
L=[]
a=list(map(int,input().split()))
for i in range(0,n):
    L.append(a[i])
    L.sort()
    if (i+1)%2==1:
        print(L[(len(L)//2)],end=" ")