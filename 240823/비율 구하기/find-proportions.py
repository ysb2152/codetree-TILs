from sortedcontainers import SortedDict
n=int(input())
sd=SortedDict()
for i in range(n):
    a=input()
    if a not in sd:
        sd[a]=1
    else:
        sd[a]+=1
for ele in sd:
    print(ele,end=" ")
    print(f"{(sd[ele]/n)*100:.4f}")