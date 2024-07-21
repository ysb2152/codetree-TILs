n=int(input())
L=[tuple(map(int,input().split()))for _ in range(n)]
distance=10000
for i in range(n):
    
    for j in range(i+1,n):
        x1,y1=L[i]
        x2,y2=L[j]
        
    distance=min(distance,((x1-x2)**2+(y1-y2)**2)**0.5)

for i in range(n):
    for j in range(i+1,n):
        x1,y1=L[i]
        x2,y2=L[j]
    dis=((x1-x2)**2+(y1-y2)**2)**0.5
    if dis==distance:
        
        print((x1-x2)**2+(y1-y2)**2)