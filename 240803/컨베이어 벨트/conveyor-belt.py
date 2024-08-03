n,t=map(int,input().split())
L=list(map(int,input().split()))
L2=list(map(int,input().split()))
def move(t):
    for _ in range(t):
        temp=L[n-1]
        temp2=L2[n-1]
        for i in range(n-1,0,-1):
            L[i]=L[i-1]
        L[0]=temp2
        for j in range(n-1,0,-1):
            L2[j]=L2[j-1]
        L2[0]=temp
move(t)
for ele in L:
    print(ele,end=" ")
print(" ")
for ele in L2:
    print(ele,end=" ")