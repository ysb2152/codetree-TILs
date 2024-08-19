import sys
n=int(input())
coin=[1,2,5]

dp=[0]*(n+1)

dp[0]=1


for i in range(1,n+1):
    for j in range(3):
        if i>=coin[j]:
            
            dp[i]=(dp[i]+dp[i-coin[j]])%10007

if dp[n]==sys.maxsize:
    print("-1")
else:
    print(dp[n])