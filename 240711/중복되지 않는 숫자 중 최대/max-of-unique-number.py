n=int(input())
L=list(map(int,input().split()))
cnt=0
k=[]
k=set(L)
k=list(k)
if len(k)==(len(L)/2):
    print("-1")
    exit()
for p in k:
    cnt=0
    for ele in L:
        if p==ele:
            
            cnt+=1
        if cnt>=2:
         
         if ele in k:
            
            k.remove(ele)
            cnt=0
        
        
if k==[]:
    print("-1")
else:
    print(max(k))