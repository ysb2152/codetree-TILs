n=int(input())
L=list(map(int,input().split()))
cnt=0

for i in range(0,n):
    if L[i]==2:
        cnt+=1
        
    if cnt==3:
        print(f"{i+1}")
        break