n=int(input())
L=[tuple(map(int,input().split()))for _ in range(n)]
L.sort(key=lambda x: (x[0]+x[1]))
L.pop(n-1)
xlayer=[]
ylayer=[]
for i in range(n-1):
    xlayer.append(L[i][0])
    ylayer.append(L[i][1])
print(max(ylayer)-min(xlayer))