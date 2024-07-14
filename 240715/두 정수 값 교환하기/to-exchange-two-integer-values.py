def ex(a,b):
    a,b=b,a
    return a,b
n,m=map(int,input().split())
n,m=ex(n,m)
print(n,end=" ")
print(m)