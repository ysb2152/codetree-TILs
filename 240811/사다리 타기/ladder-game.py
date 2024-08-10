n,m=map(int,input().split())
line=[tuple(map(int,input().split()))for _ in range(m)]
line.sort(key=lambda x: x[1])
result=[x for x in range(1,n+1)]
select_line=[]
min_cross=999999
for ele in line:
    x,y=ele
    
    result[x-1],result[x]=result[x],result[x-1]
def check():
    global min_cross
    cnt=0
    example=[x for x in range(1,n+1)]
    selected_line=[]
    for i in range(len(select_line)):
        if select_line[i]==1:
            selected_line.append(line[i])
            cnt+=1
    for ele in selected_line:
        x,y=ele
        example[x-1],example[x]=example[x],example[x-1]
    if example==result:
        min_cross=min(min_cross,cnt)

def choose(num):
    
    if num==m+1:
        
        check()
        return
            

        
    for j in range(2):
        select_line.append(j)
        choose(num+1)
        select_line.pop()
        
    return
choose(1)
print(min_cross)