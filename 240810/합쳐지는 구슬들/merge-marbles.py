# 변수 선언 및 입력:
n, m, t = tuple(map(int, input().split()))
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
next_grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
max_weight=-99999

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def next_pos(x, y,w,move_dir):
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    
    # 이동한 이후의 위치를 반환합니다.
    
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
        # 벽에 부딪히면
        # 방향을 바꾼 뒤 이동합니다.
    if not in_range(nx, ny):
        move_dir = 3 - move_dir
        return (x, y, w , move_dir)
        
        
    x, y = nx, ny

    return (x, y, w , move_dir)


def move_all():
    for x in range(n):
        for y in range(n):
            for w,num,move_dir in grid[x][y]:
                next_x, next_y, w,next_dir = next_pos(x, y, w, move_dir)
                
                next_grid[next_x][next_y].append((w, num, next_dir))
    #for row in next_grid:
        #print(row)
    #print(" ")


def select_marbles():
    global max_weight
    
    for i in range(n):
        for j in range(n):
            if len(next_grid[i][j]) > 1:
                all_w=0
                next_grid[i][j].sort(key=lambda x: (-x[1]))
                max_num=0
                #print(next_grid[i][j])
                for k in range(len(next_grid[i][j])):
                    all_w+=next_grid[i][j][k][0]
                    max_num=max(max_num,next_grid[i][j][k][1])
                max_weight=max(max_weight,all_w)
                next_grid[i][j][0]=list(next_grid[i][j][0])
                
                next_grid[i][j][0][0]=all_w
                
                next_grid[i][j]=[(next_grid[i][j][0][0],next_grid[i][j][0][1],next_grid[i][j][0][2])]
                #for row in next_grid:
                    #print(row)
                #print(" ")

            

def simulate():
    # Step1. next_grid를 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = []
		
    # Step2. 구슬들을 전부 움직입니다.
    move_all()
    
    # Step3. 각 칸마다 구슬이 최대 k개만 있도록 조정합니다.
    select_marbles()
    
    # Step4. next_grid 값을 grid로 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
    


dir_mapper = {
    "U": 0,
    "R": 1,
    "L": 2,
    "D": 3
}

for i in range(m):
    r, c, d, w = tuple(input().split())
    r, c, w = tuple(map(int, [r, c, w]))
    max_weight=max(max_weight,w)
    # 살아남는 구슬의 우선순위가 더 빠른 속도, 더 큰 번호 이므로
    # (무게, 방향, 번호) 순서를 유지합니다.
    grid[r - 1][c - 1].append((w, i + 1, dir_mapper[d]))
#for row in grid:
    #print(row)
#print(" ")

# t초에 걸쳐 시뮬레이션을 반복합니다.
for _ in range(t):
    simulate()
    #for row in grid:
        #print(row)
    #print(" ")
ans = sum([
    len(grid[i][j])
    for i in range(n)
    for j in range(n)
])


print(ans,max_weight)