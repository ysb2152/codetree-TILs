k,n=map(int,input().split())
ans=[]
def print_ans():
    for ele in ans:
        print(ele,end=" ")
    print(" ")
def choose(curr_num):
    if curr_num==n+1:
        print_ans()
        return
    for i in range(1,n+1):
        ans.append(i)
        choose(curr_num+1)
        ans.pop()
        
    return
choose(1)