n=int(input())
L=list(map(int,input().split()))
print(min(L),end=" ")
cnt=0
for ele in L:
    if ele==min(L):
        cnt+=1
print(cnt)