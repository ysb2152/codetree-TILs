n=int(input())
cnt=1
for i in range(1,n+1):
    if n==2 or n==3:
        cnt==2
        break
    cnt+=1
    n//=i
    

    
    if (n//i)<=1:
        print(f"{cnt}")
        break