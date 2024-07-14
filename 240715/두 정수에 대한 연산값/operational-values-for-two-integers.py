def comp(a,b):
    if a>b:
        return a+25,b*2
    if a<b:
        return a*2,b+25
a,b=map(int,input().split())
a,b=comp(a,b)
print(a,end=" ")
print(b)