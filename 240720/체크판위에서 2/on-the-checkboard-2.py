R,C=map(int,input().split())
grid=[]
for _ in range(R):
    a=input()
    a=list(a)
    p=[]
    for i in range(0,len(a),2):
        p.append(a[i])
    grid.append(p)
cnt=0
for i in range(1, R):
    for j in range(1, C):
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                # 그 중 색깔이 전부 달라지는 경우에만 개수를 세줍니다.
                if grid[0][0] != grid[i][j] and \
                   grid[i][j] != grid[k][l] and \
                   grid[k][l] != grid[R - 1][C - 1]:
                    cnt += 1
                        
print(cnt)