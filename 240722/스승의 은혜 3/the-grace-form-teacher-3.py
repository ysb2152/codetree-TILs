# 입력
import sys
input = sys.stdin.readline

n, b = map(int,input().split())
gift_list = [list(map(int,input().split())) for _ in range(n)]

# 계산1: 완전 탐색(쿠폰 학생)
max_res = -1
for i in range(n):

    # 1: 학생 선택
    price, fee = gift_list[i]

    # 2: 학생 적용
    temp_list = [gift_list[i][:] for i in range(n)]
    temp_list[i][0] //= 2

    # 3: 가격 정렬
    temp_list.sort(key=lambda x:(x[0]+x[1]))
    
    # 4. 최대 학생 수 할당
    sum_res = sum(temp_list[0]) if b >= sum(temp_list[0]) else 0
    j = 0 if sum_res > 0 else -1
    while j + 1 < n and sum_res + sum(temp_list[j + 1]) <= b:
        sum_res += sum(temp_list[j + 1])
        j += 1
    
    max_res = max(max_res, j + 1)

# 출력
print(max_res)