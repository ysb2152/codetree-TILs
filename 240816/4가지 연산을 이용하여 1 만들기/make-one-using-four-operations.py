from collections import deque
q=deque()
n=int(input())

visited=[]

def push(num,cnt):
    visited.append(num)
    cnt+=1
    #print(num,cnt)
    q.append((num,cnt))
def dfs():
    while q:
        num,cnt=q.popleft()
        if num==1:
            return cnt
        if num-1 not in visited:
            push(num-1,cnt)
        if num+1 not in visited and num<=(2*n)-1:
            push(num+1,cnt)
        if num//2 not in visited and num%2==0:
            push(num//2,cnt)
        if num//3 not in visited and num%3==0:
            push(num//3,cnt)
push(n,0)
print(dfs()-1)