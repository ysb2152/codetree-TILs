L=list(map(int,input().split()))
t=[]
for ele in L:
    if ele==0:
        break
    elif ele%2==0:
        t.append(ele)
print(len(t),end=" ")
print(sum(t),end=" ")