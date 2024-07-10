n=int(input())
L=list(map(int,input().split()))
cnt=0
k=set(L)
k=list(k)

for ele in k:
    for i in L:
        
        if ele==i:
            cnt+=1
    if cnt>=2:
        k.remove(i)
        cnt=0
cnt1=0

for ele in L:
    if cnt1>=2:
        print("-1")
        exit()
    if ele==max(k):
        cnt1+=1
print(max(k))