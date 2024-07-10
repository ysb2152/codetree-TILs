n=int(input())
L=list(map(int,input().split()))
cnt=0
for ele in L:
    if cnt==3:
        print(f"{L.index(ele)}")
        break
    if ele==2:
        cnt+=1