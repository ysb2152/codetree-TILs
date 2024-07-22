x,y=map(int,input().split())
cnt=0
def inter(a):
    p=[]
    a=list(map(int,list(str(a))))
    for ele in a:
        if ele not in p:
            p.append(ele)
    if len(p)==2:
        acount=a.count(p[0])
        bcount=a.count(p[1])
        if acount==1 or bcount==1:
            return 1
        else:
            return 0
    else:
        return 0
for i in range(x,y+1):
    if inter(i)==1:
        
        cnt+=1
print(cnt)