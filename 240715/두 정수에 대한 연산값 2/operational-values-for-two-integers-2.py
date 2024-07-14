def chg(a,b):
    if a<b:
        return a+10,b*2
    if a>b:
        return a*2,b+10
a,b=map(int,input().split())
a,b=chg(a,b)
print(a,end=" ")
print(b)