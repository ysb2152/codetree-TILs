L=list(map(int,input().split()))
A=[]
B=[]
for ele in L:
   if ele<500:
    A.append(ele)
   elif ele>500:
    B.append(ele)
print(max(A),end=" ")
print(min(B))