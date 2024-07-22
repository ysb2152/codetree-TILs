x,y=map(int,input().split())
cnt=0
for i in range(x,y+1):
    i=list(map(int,str(i)))
    reverse=i[::-1]
    if i==reverse:
        cnt+=1
print(cnt)