n,c,g,h=map(int,input().split())
def work(temp,ta,tb,c,g,h):
    if temp<ta:
        return c
    if ta<=temp and temp<=tb:
        return g
    if tb<temp:
        return h
t=[]
max_work=0
for j in range(n):
    ta=tuple(map(int,input().split()))
    t.append(ta)


for i in range(0,1001):
    worksum=0
    for j in range(n):
        ta,tb=t[j]
        worksum+=work(i,ta,tb,c,g,h)
    max_work=max(max_work,worksum)
print(max_work)