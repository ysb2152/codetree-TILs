n=int(input())
cnt=1
for i in range(1,8):
    
    
    if (n//(i))<=1:
        print(f"{cnt}")
        break
    n//=i
    cnt+=1