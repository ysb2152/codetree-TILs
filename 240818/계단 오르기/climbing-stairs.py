n=int(input())
dp = [0] * (n+1)
dp[0]=0
dp[1] = 1
dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

print((dp[n-1])%10007)