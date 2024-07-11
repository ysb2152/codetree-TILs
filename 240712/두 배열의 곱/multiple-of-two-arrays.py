A_arr=[list(map(int,input().split())) for _ in range(3)]
k=input()
B_arr=[list(map(int,input().split())) for _ in range(3)]


for i in range(len(A_arr)):
    for j in range(len(B_arr)):
        
        A_arr[i][j]=A_arr[i][j] * B_arr[i][j]
        print(A_arr[i][j],end=" ")
    print(" ")