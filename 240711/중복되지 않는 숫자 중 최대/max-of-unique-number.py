n=int(input())
L=list(map(int,input().split()))
cnt=0
k=[]
k=set(L)
k=list(k)
for p in k:
    cnt=0
    for ele in L:
        if p==ele:
            
            cnt+=1
        if cnt>=2:
         
         k.remove(ele)
        
if k==[]:
    print("-1")
else:
    print(max(k))