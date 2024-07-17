n=int(input())
L=[]
p=[]
cnt=0
for i in range(n):
    a=int(input())
    L.append(a)
for i in range(n):
    if n==1:
        cnt+=1
        p.append(cnt)
        cnt=0
    if L[i]>0 and L[i-1]<0:
        p.append(cnt)
        cnt=0
    if L[i]<0 and L[i-1]>0:
        p.append(cnt)
        cnt=0
    if i==n-1:
        p.append(cnt)
        cnt=0
    cnt+=1
print(max(p))