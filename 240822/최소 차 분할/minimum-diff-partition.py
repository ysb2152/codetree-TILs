n = int(input())

nums = list(map(int, input().split()))

s = sum(nums)

dp = [False] * (s + 1)

dp[nums[0]] = True

for i in range(1, n):
    num = nums[i]
    _nums = []
    for j in range(s):
        if dp[j]:
            dp[j] = False
            _nums.append(abs(j - num))
            _nums.append(j + num)
    for _num in _nums:
        dp[_num] = True

ans = 0

for i in range(s + 1):
    if dp[i]:
        ans = i
        break

print(ans)