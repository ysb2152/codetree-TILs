n=int(input())
nums=[list(map(int,input().split()))for _ in range(4)]
dict1={}
cnt=0
for i in range(n):
    for j in range(n):
        if nums[0][i]+nums[1][j] not in dict1:
            dict1[nums[0][i]+nums[1][j]]=1
        else:
            dict1[nums[0][i]+nums[1][j]]+=1
for i in range(n):
    for j in range(n):
        if -nums[2][i]-nums[3][j] in dict1:
            cnt+=dict1[-nums[2][i]-nums[3][j]]
print(cnt)