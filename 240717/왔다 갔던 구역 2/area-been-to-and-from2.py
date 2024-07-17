n=int(input())
L=[0 for _ in range(21)]

for _ in range(n):
    a,b=input().split()
    a=int(a)
    start=11
    if b=='L':
        for i in range(start,start-a,-1):
            L[i]+=1
    if b=='R':
        for i in range(start,start+a):
            L[i]+=1
print(max(L))