n=int(input())
cnt=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{cnt}",end=" ")
        cnt+=1
    print(" ")