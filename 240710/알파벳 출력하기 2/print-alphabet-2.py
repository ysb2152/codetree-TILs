n=int(input())
cnt=65
for i in range(0,n):
    print("  "*i,end="")
    for j in range(n-i):
        if cnt>89:
            cnt=65
        
        print(f"{chr(cnt)}",end=" ")
        cnt+=1
    print(" ")