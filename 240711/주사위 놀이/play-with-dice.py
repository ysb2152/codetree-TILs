L=list(map(int,input().split()))
k=[0 for _ in range(6)]

for ele in L:
    k[ele-1]+=1

for i in range(0,len(k)):
    print(f"{i+1} - {k[i]}")