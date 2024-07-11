# 변수 선언 및 입력:
n = int(input())
price = list(map(int, input().split()))

# 배열을 앞에서부터 순회하며 사는 시점의 후보를 선택합니다
max_profit = 0
for i in range(n):
    # 사는 시점의 다음 해부터 순회하며 파는 시점의 후보를 선택합니다
    for j in range(i + 1, n):
        profit = price[j] - price[i]

        if profit > max_profit:
            max_profit = profit
    
print(max_profit)