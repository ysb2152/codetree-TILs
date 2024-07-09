L=list(map(int,input().split()))
T=[]
for ele in L:
    if ele==0:
        break
    T.append(ele)
print(f"{sum(T)}",end=" ")
print(f"{(sum(T)/len(T)):.1f}")