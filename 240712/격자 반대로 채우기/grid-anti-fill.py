n=int(input())
L=[[0 for _ in range(n)] for _ in range(n)]
cnt=1
for j in range(n-1,-1,-1):
    
        if j%2==1:
            for i in range(n-1,-1,-1):
                L[i][j]=L[i][j]+cnt
                cnt+=1
        else:
            for i in range(0,n):
                L[i][j]=L[i][j]+cnt
                cnt+=1


    
for row in L:
    for ele in row:
        print(ele,end=" ")
    print(" ")