from sortedcontainers import SortedSet
ss=SortedSet()
T=int(input())
for _ in range(T):
    k=int(input())
    for _ in range(k):
        a=input()
        if a.startswith('I'):
            _,n=a.split()
            n=int(n)
            ss.add(n)
        if a.startswith('D'):
            if len(ss)==0:
                continue
            else:
                _,n=a.split()
                n=int(n)
                if n==1:
                    ss.remove(ss[-1])
                elif n==-1:
                    ss.remove(ss[0])
    if len(ss)==0:
        
        print("EMPTY")
    else:
        print(ss[-1],end=" ")
        print(ss[0])
    ss=SortedSet()