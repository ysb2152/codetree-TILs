a,b=map(int,input().split())
c=[]
d=a
e=b
for _ in range(21):
    a=(a-(a//b)*b)*10
    c.append(a//b)

print(f"{d//e}.",end="")
for i in range(0,20):
    print(f"{c[i]}",end="")