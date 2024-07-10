L=list(map(int,input().split()))
for ele in L:
    if ele==999 or ele==-999:
        
        L=L[:L.index(ele)]

print(max(L),end=" ")
print(min(L))