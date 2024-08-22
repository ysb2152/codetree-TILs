# 필요한 상수를 정의합니다.
MOD = 10**9 + 7
MAXN = 1005

# n 값을 입력받습니다.
n = int(input())

# 동적 프로그래밍 배열을 초기화합니다.
dp = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(MAXN)]

# 초기 상태를 설정합니다.
dp[1][1][0] = 1  # 첫 번째 날에 T를 받은 경우
dp[1][0][1] = 1  # 첫 번째 날에 B를 받은 경우
dp[1][0][0] = 1  # 첫 번째 날에 G를 받은 경우

# 동적 프로그래밍을 사용해 문제를 해결합니다.
# dp[i][j][k] :: i번째 날에, T를 총합 j회 받았고, B를 최근 k회 연속 받은 경우의 가짓수
for i in range(1, n):
    for j in range(3):
        for k in range(3):
            # 다음 날로 넘어가는 경우의 수를 갱신합니다.
            dp[i + 1][j + 1][0] = (dp[i + 1][j + 1][0] + dp[i][j][k]) % MOD
            dp[i + 1][j][0] = (dp[i + 1][j][0] + dp[i][j][k]) % MOD
            if k < 2:
                dp[i + 1][j][k + 1] = (dp[i + 1][j][k + 1] + dp[i][j][k]) % MOD

# 최종 결과를 계산합니다.
ans = 0
for j in range(3):
    for k in range(3):
        ans = (ans + dp[n][j][k]) % MOD

# 결과를 출력합니다.
print(ans)