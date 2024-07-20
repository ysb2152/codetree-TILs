n=int(input())
a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())
open1=[]
o=[[],[],[]]
p=[[],[],[]]
cnt=0
result=[]
for i in range(1,n+1):
    if abs(i-a1)<=2 or (i==n and a1<=2) or (i==n-1 and a1==1) or (a1==n and i<=2) or (a1==n-1 and i==1):
        o[0].append(i)
for j in range(1,n+1):
    if abs(j-b1)<=2 or (j==n and b1<=2) or (j==n-1 and b1==1) or (b1==n and j<=2) or (b1==n-1 and j==1):
        o[1].append(j)
for k in range(1,n+1):
    if abs(k-c1)<=2 or (k==n and c1<=2) or (k==n-1 and c1==1) or (c1==n and k<=2) or (c1==n-1 and k==1):
        o[2].append(k)



for i in range(1,n+1):
    if abs(i-a2)<=2 or (i==n and a2<=2) or (i==n-1 and a2==1) or (a2==n and i<=2) or (a2==n-1 and i==1):
        p[0].append(i)
for j in range(1,n+1):
    if abs(j-b2)<=2 or (j==n and b2<=2) or (j==n-1 and b2==1) or (b2==n and j<=2) or (b2==n-1 and j==1):
        p[1].append(j)
for k in range(1,n+1):
    if abs(k-c2)<=2 or (k==n and c2<=2) or (k==n-1 and c2==1) or (c2==n and k<=2) or (c2==n-1 and k==1):
        p[2].append(k)

for a in range(len(o[0])):
    for b in range(len(o[1])):
        for c in range(len(o[2])):
            if [o[0][a],o[1][b],o[2][c]] in open1:
                continue
            open1.append([o[0][a],o[1][b],o[2][c]])
for a in range(len(p[0])):
    for b in range(len(p[1])):
        for c in range(len(p[2])):
            if [p[0][a],p[1][b],p[2][c]] in open1:
                continue
            open1.append([p[0][a],p[1][b],p[2][c]])
print(len(open1))