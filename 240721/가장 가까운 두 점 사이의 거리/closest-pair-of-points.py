import sys
n=int(input())
L=[tuple(map(int,input().split()))for _ in range(n)]
distance=sys.maxsize
def dist(i, j):
    x1, y1 = L[i]
    x2, y2 = L[j]
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
for i in range(n):
    for j in range(i+1,n):
        distance=min(distance,dist(i,j))
print(distance)