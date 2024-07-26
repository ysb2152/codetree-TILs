n=int(input())
L=[int(input())for _ in range(n)]
mid=sum(L)//n
cnt=0
for i in range(n):
    if L[i]>mid:
        cnt+=L[i]-mid
print(cnt)