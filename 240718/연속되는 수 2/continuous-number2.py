n=int(input())
cnt=0
L=[]
p=[]
for i in range(n):
    a=int(input())
    L.append(a)
for i in range(n):
    if n==1:
        p.append(cnt)
        cnt=0
    if L[i]!=L[i-1]:
        p.append(cnt)
        cnt=0
    if i==n-1:
        cnt+=1
        p.append(cnt)
        cnt=0
        
    cnt+=1
print(max(p))