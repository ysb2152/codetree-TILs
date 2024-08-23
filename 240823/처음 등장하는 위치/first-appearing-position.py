from sortedcontainers import SortedDict
sd=SortedDict()
n=int(input())
L=list(map(int,input().split()))
for i in range(n):
    
    a=L[i]
    if a not in sd:
        sd[a]=i+1
for ele in sd:
    print(ele,end=" ")
    print(sd[ele])