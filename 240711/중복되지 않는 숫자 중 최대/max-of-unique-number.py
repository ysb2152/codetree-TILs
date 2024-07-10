n=int(input())
L=list(map(int,input().split()))
L=set(L)
L=list(L)
cnt=0
for ele in L:
    if cnt>=2:
        print("-1")
        exit()
    if max(L)==ele:
        cnt+=1
print(max(L))