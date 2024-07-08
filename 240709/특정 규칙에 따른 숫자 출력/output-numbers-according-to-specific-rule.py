n=int(input())
cnt=1
for i in range(0,n):
    print(" "*2*i,end="")
    for j in range(1,n+1):

        if i<=n-j:
            print(f"{cnt}",end=" ")
            cnt+=1
        if cnt>9:
            cnt=1
    print(" ")