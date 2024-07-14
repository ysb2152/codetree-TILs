def mul(n):
    for i in range(0,len(n)):
        if n[i]<0:
            n[i]=n[i]*-1
            print(n[i],end=" ")
        else:
            print(n[i],end=" ")
N=int(input())
L=list(map(int,input().split()))
mul(L)