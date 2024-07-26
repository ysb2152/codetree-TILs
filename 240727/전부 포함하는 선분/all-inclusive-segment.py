n=int(input())
L=[tuple(map(int,input().split()))for _ in range(n)]
L.sort()


t=[]
s=[]
t.sort(key=lambda x: x[1])
for i in range(n):
    s.append(L[i])
for i in range(n):
    t.append(L[i])
t.pop(n-1)
L.pop(n-1)
xlayer=[]
ylayer=[]
x1layer=[]
y1layer=[]

for i in range(n-1):
    xlayer.append(L[i][0])
    ylayer.append(L[i][1])
for i in range(n-1):
    xlayer.append(L[i][0])
    ylayer.append(L[i][1])
for i in range(n-1):
    x1layer.append(t[i][0])
    y1layer.append(t[i][1])
for i in range(n-1):
    x1layer.append(t[i][0])
    y1layer.append(t[i][1])

print(min(max(ylayer)-min(xlayer),max(y1layer)-min(x1layer)))