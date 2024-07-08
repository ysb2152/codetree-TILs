n=int(input())
cnt=9
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{cnt}",end="")
        cnt-=1
        if cnt==0:
            cnt=9
    print(" ")