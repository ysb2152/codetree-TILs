L=[list(map(int,input().split())) for _  in range(19)]
cnt=0
def in_range(a,b):
    return 0<=a and a<19 and 0<=b and b<19
for i in range(19):
    for j in range(19):
        if in_range(i,j+1) and in_range(i,j+2) and in_range(i,j+3) and in_range(i,j+4) and L[i][j]==1 and L[i][j+1]==1 and L[i][j+2]==1 and L[i][j+3]==1 and L[i][j+4]==1:
            print("1")
            print(i+1,j+3)
            cnt+=1
        if in_range(i,j+1) and in_range(i,j+2) and in_range(i,j+3) and in_range(i,j+4) and L[i][j]==2 and L[i][j+1]==2 and L[i][j+2]==2 and L[i][j+3]==2 and L[i][j+4]==2:
            print("2")
            print(i+1,j+3)
            cnt+=1
        if in_range(i+1,j) and in_range(i+2,j) and in_range(i+3,j) and in_range(i+4,j) and L[i][j]==1 and L[i+1][j]==1 and L[i+2][j]==1 and L[i+3][j]==1 and L[i+4][j]==1:
            print("1")
            print(i+3,j+1)
            cnt+=1
        if in_range(i+1,j) and in_range(i+2,j) and in_range(i+3,j) and in_range(i+4,j) and L[i][j]==2 and L[i+1][j]==2 and L[i+2][j]==2 and L[i+3][j]==2 and L[i+4][j]==2:
            print("2")
            print(i+3,j+1)
            cnt+=1
        if in_range(i+1,j+1) and in_range(i+2,j+2) and in_range(i+3,j+3) and in_range(i+4,j+4) and L[i][j]==1 and L[i+1][j+1]==1 and L[i+2][j+2]==1 and L[i+3][j+3]==1 and L[i+4][j+4]==1:
            print("1")
            print(i+3,j+3)
            cnt+=1
        if in_range(i+1,j+1) and in_range(i+2,j+2) and in_range(i+3,j+3) and in_range(i+4,j+4) and L[i][j]==2 and L[i+1][j+1]==2 and L[i+2][j+2]==2 and L[i+3][j+3]==2 and L[i+4][j+4]==2:
            print("2")
            print(i+3,j+3)
            cnt+=1
        if in_range(i-1,j+1) and in_range(i-2,j+2) and in_range(i-3,j+3) and in_range(i-4,j+4) and L[i][j]==1 and L[i-1][j+1]==1 and L[i-2][j+2]==1 and L[i-3][j+3]==1 and L[i-4][j+4]==1:
            print("1")
            print(i-1,j+3)
            cnt+=1
        if in_range(i-1,j+1) and in_range(i-2,j+2) and in_range(i-3,j+3) and in_range(i-4,j+4) and L[i][j]==2 and L[i-1][j+1]==2 and L[i-2][j+2]==2 and L[i-3][j+3]==2 and L[i-4][j+4]==2:
            print("2")
            print(i-1,j+3)
            cnt+=1
if cnt==0:
    print("0")