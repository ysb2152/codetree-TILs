def div1(n):
    for i in range(0,len(n)):
        if (n[i])%2==0:
            n[i]/=2
        print(f"{n[i]:.0f}",end=" ")
n=int(input())
L=list(map(int,input().split()))

div1(L)