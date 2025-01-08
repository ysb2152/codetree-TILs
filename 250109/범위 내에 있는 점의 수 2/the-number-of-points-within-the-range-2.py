n, q = map(int, input().split())
points = list(map(int, input().split()))
ranges = [tuple(map(int, input().split())) for _ in range(q)]
lines=[0 for _ in range(1000001)]
prefix=[0 for _ in range(1000001)]
for i in range(len(points)):
    lines[points[i]]=1
#print(lines)
cnt=0
for i in range(len(prefix)):
    if lines[i]!=0:
        cnt+=1
    prefix[i]=cnt
for i in range(len(ranges)):
    a,b=ranges[i]
    print(prefix[b]-prefix[a]+lines[a])

