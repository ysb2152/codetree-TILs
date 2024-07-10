n=int(input())
L=list(map(int,input().split()))
cnt=0
k=[]
k=set(L)
k=list(k)
for i in range(0,len(k)-1):
    cnt=0
    for ele in L:
        if k[i]==ele:
            
            cnt+=1
        if cnt>=2:
         
         k.remove(ele)
        
if k==[]:
    print("-1")
else:
    print(max(k))