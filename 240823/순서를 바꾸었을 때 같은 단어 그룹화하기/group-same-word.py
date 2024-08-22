n=int(input())
arr=[]
dic=dict()
max_cnt=-999
for i in range(n):

    a=input()
    
    a=list(a)
    a.sort()
    a=''.join(a)
    arr.append(a)
    if a not in dic:
        dic[a]=1
    else:
        dic[a]+=1
for ele in arr:
    
    max_cnt=max(max_cnt,dic[ele])
print(max_cnt)