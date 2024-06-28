n=int(input())
cnt=0
for i in range(1,n+1):
    n//=i
    cnt+=1
    if (n//i)<=1:
        print(f"{cnt+1}")
        break