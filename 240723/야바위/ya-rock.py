n=int(input())
a1=[1,0,0]
a2=[0,1,0]
a3=[0,0,1]
cnt1=0
cnt2=0
cnt3=0
L=[]
for i in range(n):
    a,b,c=list(map(int,input().split()))
    L.append([a,b,c])

for j in range(n):
    
    p,q,r=L[j][0],L[j][1],L[j][2]
    
    p-=1
    q-=1
    r-=1
    
    pr=a1[p]
    a1[p]=a1[q]
    a1[q]=pr
    
    if a1[r]==1:
        cnt1+=1

for k in range(n):
    p,q,r=L[k][0],L[k][1],L[k][2]
    p-=1
    q-=1
    r-=1
    pr=a2[p]
    a2[p]=a2[q]
    a2[q]=pr
    if a2[r]==1:
        cnt2+=1
for l in range(n):
    p,q,r=L[l][0],L[l][1],L[l][2]
    p-=1
    q-=1
    r-=1
    pr=a3[p]
    a3[p]=a3[q]
    a3[q]=pr
    if a3[r]==1:
        cnt3+=1
print(max(cnt1,cnt2,cnt3))