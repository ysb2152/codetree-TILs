L=list(map(int,input().split()))
k=[0 for _ in range(100)]


for ele in L:
    if ele==0:
        break
    elif ele<10:
        continue
    
    k[(ele//10)]+=1
    

for i in range(100,0,-10):
    print(f"{i} - {k[(i//10)]}")