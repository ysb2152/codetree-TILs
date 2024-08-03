n,t=map(int,input().split())
L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
L3=list(map(int,input().split()))
for _ in range(t):
    temp=L1[n-1]
    temp2=L2[n-1]
    temp3=L3[n-1]
    for i in range(n-1,0,-1):
        L1[i]=L1[i-1]
    
    for i in range(n-1,0,-1):
        L2[i]=L2[i-1]
    
    for i in range(n-1,0,-1):
        L3[i]=L3[i-1]
    L2[0]=temp
    L3[0]=temp2
    L1[0]=temp3
for ele in L1:
    print(ele,end=" ")
print(" ")
for ele in L2:
    print(ele,end=" ")
print(" ")
for ele in L3:
    print(ele,end=" ")