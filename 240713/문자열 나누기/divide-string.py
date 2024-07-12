n=int(input())
c=input().split()
c=''.join(c)
cnt=0
for ele in c:
    print(ele,end="")
    cnt+=1
    if cnt%5==0:
        print(" ")