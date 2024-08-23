from sortedcontainers import SortedDict
sd=SortedDict()
n=int(input())
for _ in range(n):
    a=input()
    if a not in sd:
        sd[a]=1
    else:
        sd[a]+=1
for ele in sd:
    print(ele,end=" ")
    print(sd[ele])