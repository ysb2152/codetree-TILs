from sortedcontainers import SortedSet

n=int(input())
arr=[]
for _ in range(n):
    a=tuple(map(int,input().split()))
    c,d=a
    arr.append((d,c))
ss=SortedSet(arr)
m=int(input())
for _ in range(m):
    order=input()
    if order.startswith("rc"):
        _,x=order.split()
        x=int(x)
        if x==1:
            print(ss[-1][1])
            continue
        if x==-1:
            print(ss[0][1])
            continue
    if order.startswith("ad"):
        _,P,L=order.split()
        P,L=int(P),int(L)
        ss.add((L,P))
    if order.startswith("sv"):
        _,P,L=order.split()
        P,L=int(P),int(L)
        ss.remove((L,P))