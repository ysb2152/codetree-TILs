L=list(map(int,input().split()))
k=[0 for _ in range(9)]
for ele in L:
    if ele==0:
        break
    if (ele//10)==0:
        continue
    k[(ele//10)-1]+=1
for i in range(0,9):
    print(f"{i+1} - {k[i]}")