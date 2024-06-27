a,b=map(int,input().split())
c=[]
for _ in range(21):
    a=(a-(a//b)*b)*10
    c.append(a//b)
print("0.",end="")
for i in range(0,20):
    print(f"{c[i]}",end="")