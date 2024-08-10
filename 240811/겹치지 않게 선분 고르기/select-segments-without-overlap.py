n=int(input())
L=[tuple(map(int,input().split()))for _ in range(n)]
ans=[]
max_cnt=-99999
def print_ans():
    global max_cnt
    cnt=0
    temp=[0 for _ in range(10)]
    for i in range(n):
        if ans[i]==1:
            a,b=L[i]
            for j in range(a,b+1):
                temp[j]+=1
            for k in range(len(temp)):
                if temp[k]>1:
                    return cnt
            cnt+=1
        max_cnt=max(max_cnt,cnt)
def choose(curr_num):
    if curr_num==n+1:
        print_ans()
        return
    for i in range(2):
        ans.append(i)
        choose(curr_num+1)
        ans.pop()
                
    return
choose(1)
print(max_cnt)