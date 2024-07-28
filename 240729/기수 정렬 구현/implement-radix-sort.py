n=int(input())
L=list(map(int,input().split()))
leng=len(str(L[0]))
for k in range(leng-1,-1,-1):
    arr_new=[[] for _ in range(10)]
    for i in range(len(L)):
        L[i]=str(L[i])
        digit=L[i][k]
        
        digit=int(digit)
        
        L[i]=int(L[i])
        arr_new[digit].append(L[i])
    store=[]
    for i in range(10):
        for j in range(len(arr_new[i])):
            store.append(arr_new[i][j])
    L=store
for ele in L:
    print(ele,end=" ")