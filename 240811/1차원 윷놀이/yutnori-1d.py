n,m,k=map(int,input().split())
turn=list(map(int,input().split()))
area=[i for i in range(1,m+1)]
max_ap=-99999
#명령을 수행할 말
horse=[1 for _ in range(k)]
def count():
    global max_ap
    cnt=0
    for i in range(k):
        if horse[i]>=m:
            cnt+=1
    max_ap=max(max_ap,cnt)
    
    
        
def choose(num):
    if num==n:
        count()
        return
    for i in range(k):
        horse[i]+=turn[num]
        choose(num+1)
        horse[i]-=turn[num]
        
    return
choose(0)
print(max_ap)