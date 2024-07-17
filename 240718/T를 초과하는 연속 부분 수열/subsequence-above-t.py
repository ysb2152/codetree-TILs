n,t=map(int,input().split())
L=list(map(int,input().split()))
p=[]
cnt=0
for i in range(n):
    if n==1:
        if L[0]>t:
            cnt+=1
        else:
            cnt=0
        p.append(cnt)
        cnt=0
    if L[i]<=t:
        cnt-=1
        p.append(cnt)
        cnt=0
    if i==n-1:
        cnt+=1
        p.append(cnt)
        cnt=0
    cnt+=1
print(max(p))