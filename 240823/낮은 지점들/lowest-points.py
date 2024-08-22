n=int(input())
dic={}
xs=[]
cnt=0
for _ in range(n):
    x,y=map(int,input().split())
    if x not in dic:
        dic[x]=y
        xs.append(x)
    else:
        if dic[x]>y:
            dic[x]=y
for ele in xs:
    cnt+=dic[ele]
print(cnt)