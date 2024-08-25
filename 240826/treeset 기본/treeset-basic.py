from sortedcontainers import SortedSet
n=int(input())
ss=SortedSet()
for _ in range(n):
    a=input()
    if a.startswith("add"):
        _,x=a.split()
        x=int(x)
        if x in ss:
            continue
        else:
            ss.add(x)
            
            continue
    if a.startswith("remove"):
        _,x=a.split()
        x=int(x)
        ss.remove(x)
        continue
    if a.startswith("find"):
        _,x=a.split()
        x=int(x)
        if x in ss:
            print("true")
            continue
        else:
            print("false")
            continue
    if a.startswith("lower_bound"):
        _,x=a.split()
        x=int(x)
        if ss.bisect_left(x)==len(ss):
            print("None")
            continue
        else:
            print(ss[ss.bisect_left(x)])
            continue
    if a.startswith("upper_bound"):
        _,x=a.split()
        x=int(x)
        if ss.bisect_right(x)==len(ss):
            print("None")
            continue
        else:
            print(ss[ss.bisect_right(x)])
            continue
    if a.startswith("largest"):
        if len(ss)==0:
            print("None")
            continue
        else:
            print(ss[-1])
            continue
    if a.startswith("smallest"):
        if len(ss)==0:
            print("None")
            continue
        else:
            print(ss[0])
            continue