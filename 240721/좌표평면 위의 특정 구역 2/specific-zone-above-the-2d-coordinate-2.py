n=int(input())
L=[tuple(map(int,input().split()))for _ in range(n)]

area=[0 for _ in range(n)]
for i in range(n):
    compx=[]
    compy=[]
    for j in range(n):
        if j==i:
            continue
        x,y=L[j]
        
        compx.append(x)
        compy.append(y)
    
    xline=max(compx)-min(compx)
    
    yline=max(compy)-min(compy)
    
    area[i]=xline*yline
print(min(area))