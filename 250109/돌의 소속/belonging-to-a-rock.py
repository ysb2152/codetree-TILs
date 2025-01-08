N, Q = map(int, input().split())
arr = [int(input()) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]
prefix1=[0 for _ in range(N)]
prefix2=[0 for _ in range(N)]
prefix3=[0 for _ in range(N)]
# Write your code here!
arr1=[]
arr2=[]
arr3=[]
for ele in arr:
    if ele==1:
        arr1.append(1)
    else:
        arr1.append(0)
for ele in arr:
    if ele==2:
        arr2.append(1)
    else:
        arr2.append(0)
for ele in arr:
    if ele==3:
        arr3.append(1)
    else:
        arr3.append(0)
cnt1=0
cnt2=0
cnt3=0
for i in range(len(arr)):
    if arr[i]==1:
        cnt1+=1
    prefix1[i]=cnt1
for i in range(len(arr)):
    if arr[i]==3:
        cnt3+=1
    prefix3[i]=cnt3
for i in range(len(arr)):
    if arr[i]==2:
        cnt2+=1
    prefix2[i]=cnt2
for ele in queries:
    a,b=ele
    a-=1
    b-=1
    print((prefix1[b]-prefix1[a]+arr1[a]),(prefix2[b]-prefix2[a]+arr2[a]),(prefix3[b]-prefix3[a]+arr3[a]))
    
