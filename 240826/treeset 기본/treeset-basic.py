from sortedcontainers import SortedSet
n=int(input())
ss=SortedSet()
for _ in range(n):
    a=input()
    if a.startswith("add"):
        _,x=a.split()
        if x in ss:
            continue
        else:
            ss.add(x)
    if a.startswith("remove"):
        _,x=a.split()
        ss.remove(x)
    if a.startswith("find"):
        _,x=a.split()
        if x in ss:
            print("true")
        else:
            print("false")
    if a.startswith("lower_bound"):
        _,x=a.split()
        if ss.bisect_left(x)==len(ss):
            print("None")
        else:
            print(ss[ss.bisect_left(x)])
    if a.startswith("upper_bound"):
        _,x=a.split()
        if ss.bisect_right(x)==len(ss):
            print("None")
        else:
            print(ss[ss.bisect_right(x)])
    if a.startswith("largest"):
        if len(ss)==0:
            print("None")
        else:
            print(ss[-1])
    if a.startswith("smallest"):
        if len(ss)==0:
            print("None")
        else:
            print(ss[0])