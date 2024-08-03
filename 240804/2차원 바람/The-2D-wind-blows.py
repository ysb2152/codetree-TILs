n, m, q = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

d_rows, d_cols = [0, 1, 0, -1], [1, 0, -1, 0];

def coord_to_data(coord):
    row, col = coord
    return grid[row][col]

def around_value_avg(coord):
    row, col = coord
    total = grid[row][col]
    cnt = 1

    for d_row, d_col in zip(d_rows, d_cols):
        n_row = row + d_row
        n_col = col + d_col

        if n_row < 0 or n <= n_row:
            continue
        if n_col < 0 or m <= n_col:
            continue
        
        total += grid[n_row][n_col]
        cnt += 1

    return total // cnt


for _ in range(q):
    start_row, start_col, end_row, end_col = map(int, input().split())
    start_row, start_col = start_row - 1, start_col - 1
    end_row, end_col = end_row - 1, end_col - 1
    coord_list = []

    piv = 0

    end_point = [start_row, start_col]
    cur = end_point[:]
    coord_list.append(cur[:])

    while piv < 4:
        d_row, d_col = d_rows[piv], d_cols[piv]
        n_row = cur[0] + d_row
        n_col = cur[1] + d_col

        if n_row < start_row or end_row < n_row:
            piv += 1
            continue
        if n_col < start_col or end_col < n_col:
            piv += 1
            continue
        
        if end_point[0] == n_row and end_point[1] == n_col:
            piv += 1
            continue
        
        cur = [n_row, n_col]
        coord_list.append(cur[:])
    
    n_coord_data_list = list(map(coord_to_data, coord_list))
    n_coord_data_list.insert(0, n_coord_data_list.pop())

    for i in range(len(coord_list)):
        row, col = coord_list[i]
        grid[row][col] = n_coord_data_list[i]
    
    coord_list = []

    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            coord_list.append([row, col])

    n_coord_avg_list = list(map(around_value_avg, coord_list))

    for i in range(len(coord_list)):
        row, col = coord_list[i]
        grid[row][col] = n_coord_avg_list[i]


for row in grid:
    print(" ".join(map(str, row)))