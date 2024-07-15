n=int(input())
L=list(map(int,input().split()))
L.sort()
t=[]
p=[]
for i in range(len(L)):
    if i%2==0:
        p.append(L[i])
    if i%2==1:
        t.append(L[i])
cnt=0  
cnt1=0         
for ele in t:
    cnt+=ele
for ele in p:
    cnt1+=ele
if cnt>=cnt1:
    print(cnt)
else:
    print(cnt1)