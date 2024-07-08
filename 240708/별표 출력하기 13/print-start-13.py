n=int(input())
cnt1=n
cnt2=1
for i in range(0,2*n):
    if i%2==0:
        for _ in range(cnt1):
            print("*",end=" ")
        print(" ")
        cnt1-=1
    if i%2==1:
        for _ in range(cnt2):
            print("*",end=" ")
        print(" ")
        cnt2+=1