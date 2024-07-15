n=int(input())
L=list(map(int,input().split()))
L.sort()
t=[]
p=[]
cnt=0
for i in range(len(L)):
    cnt1=L[i]+L[2*n-1-i]
    if cnt1>cnt:
        cnt=cnt1
print(cnt)