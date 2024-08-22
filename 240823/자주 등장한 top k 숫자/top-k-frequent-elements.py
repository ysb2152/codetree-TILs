n,k=map(int,input().split())
arr=list(map(int,input().split()))
count={}
setarr=set(arr)
countarr=[]
for ele in arr:
    if ele in count:
        count[ele]+=1
    else:
        count[ele]=1
for ele in setarr:
    countarr.append((count[ele],ele))
countarr.sort(key=lambda x:(-x[0],-x[1]))
for i in range(k):
    print(countarr[i][1],end=" ")