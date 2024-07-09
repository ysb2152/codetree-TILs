n=int(input())
cnt=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(f"{chr(cnt)}",end="")
        cnt+=1
    print(" ")