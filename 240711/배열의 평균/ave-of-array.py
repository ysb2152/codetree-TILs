L=[list(map(int,input().split())) for _ in range(2)]
g=0
s=0
a=0
for i in range(0,2):
    for j in range(0,4):
        g+=L[i][j]
        a+=L[i][j]
    print(f"{(g/4):.1f}",end=" ")
    g=0
print(" ")
for i in range(0,4):
    for j in range(0,2):
        s+=L[j][i]
    print(f"{(s/2):.1f}",end=" ")
    s=0
print(" ")
print(f"{(a/8):.1f}")