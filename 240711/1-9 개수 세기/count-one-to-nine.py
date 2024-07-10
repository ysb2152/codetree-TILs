n=int(input())
L=list(map(int,input().split()  ))
k=[0 for _ in range(9)]
for ele in L:
    k[ele-1]+=1

for i in range(0,9):
    print(k[i])