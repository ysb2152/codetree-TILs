n=int(input())
cnt=1
cnt1=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2==1:
            print(f"{cnt}",end=" ")
            cnt+=1
        else:
            if j==1:
                cnt1=cnt+n
            print(f"{cnt+n-1}",end=" ")
            cnt-=1
            if j==n:
                cnt=cnt1
    print(" ")