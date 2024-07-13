a,b=map(int,input().split())
c=a+b
c=str(c)
c=list(c)
cnt=0
for ele in c:
    if ele=='1':
        cnt+=1
print(cnt)