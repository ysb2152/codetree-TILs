n=int(input())
curr=50000
L=[0 for _ in range(100000)]
for _ in range(n):
    x,direction=input().split()
    x=int(x)
    if direction=='L':
        left=curr-x
        right=curr
        curr-=x
        for i in range(left,right):
            L[i]='W'
    if direction=='R':
        left=curr
        right=curr+x
        curr+=x
        for i in range(left,right):
            L[i]='B'
Blackcnt=0
Whitecnt=0

for ele in L:
    if ele=='B':
        Blackcnt+=1
    if ele=='W':
        Whitecnt+=1

print(Whitecnt,Blackcnt)