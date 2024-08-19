import sys
n = int(input())
si = list(map(int,input().split()))


arr = [0] + si

# 만들 수 있는 최대 합 m을 계산
m = sum(arr)

# dp[i][j]: 지금까지 i번째 수까지만 고려해봤을 때, 고른 수의 합을 j로 만드는 것이 가능하면 True, 불가능하면 False
dp = [[0] * (m + 1) for _ in range(n + 1)]


def preprocess():
    dp[0][0] = True


preprocess()

for i in range(1, n + 1):
    for j in range(m + 1):
        # Case 1:
        # i번째 수를 선택하여 합이 j가 된 경우
        # i - 1번째까지 고려하여 고른 수들의 합이 j - arr[i]
        if j >= arr[i] and dp[i - 1][j - arr[i]]:
            dp[i][j] = j

        # Case 2:
        # i번째 수를 선택하지 않고 합이 j가 된 경우
        # i번째 수를 제외하고 합이 j
        # i - 1번째까지 고려하여 고른 수의 합이 j
        if dp[i - 1][j]:
            dp[i][j] = j

# n개의 수까지 전부 고려했을 데
# 그룹 A에 대해 정확히 합 i를 만들 수 있다면,
# j / m - j 이렇게 두 그룹으로 나눌 수 있다는 뜻
ans = "No"
for j in range(1, m):
    if dp[n][j] == m-j:
        ans = "Yes"
        break
print(ans)