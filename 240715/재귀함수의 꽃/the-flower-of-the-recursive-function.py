def comp(n):
    if n==0:
        return
    print(n,end=" ")
    comp(n-1)
    print(n,end=" ")
N=int(input())
comp(N)