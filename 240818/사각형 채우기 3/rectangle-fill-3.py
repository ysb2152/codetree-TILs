n=int(input())
memo=[0 for _ in range(n+2)]
memo[0]=1
memo[1]=2
memo[2]=7
for i in range(3,n+1):
    memo[i]=memo[i-1]*3 + memo[i-2] - memo[i-3]
print(memo[n])