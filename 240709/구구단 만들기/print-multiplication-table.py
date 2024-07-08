a,b=map(int,input().split())
cnt=0

for i in range(1,10):
    for j in range(b,a-1,-1):
        if j%2==0:
            print(f"{j} * {i} = {j*i} ",end="")
            cnt+=1
        if j<2 and j%2==0:
            print("/",end=" ")
    print(" ")