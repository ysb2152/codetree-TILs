import sys
n=int(input())
L=list(map(int,input().split()))
numlist=[i for i in range(2*n)]

min_cnt=sys.maxsize
ans1=[]
def summ(ans):
    cnt=0
    for i in range(n):
        cnt+=L[ans[i]]
    return cnt


def choose(num,cnt):
    global min_cnt
    ans2=[]
    if num==n+1:
        for j in range(2*n):
            if j not in ans1:
                ans2.append(j)
        #print(ans1)
        #print(ans2)
        min_cnt=min(min_cnt,abs(summ(ans1)-summ(ans2)))
        return
    for i in range(cnt,2*n):
        if i not in ans1:
            ans1.append(i)
            choose(num+1,i)
            ans1.pop()
    return
choose(1,0)
print(min_cnt)