n = int(input())
dp = [0] * 10000000

def test(n) : 
    dp[1] = 1
    dp[2] = 2
    dp[3] = 5
    
    if dp[n] != 0 :
        return dp[n]

    if n <= 1 :
        return 1

    temp = 0
    for i in range(n) :
        temp += test(i) * test(n - i - 1)
    dp[n] = temp
    return dp[n]

print(test(n))