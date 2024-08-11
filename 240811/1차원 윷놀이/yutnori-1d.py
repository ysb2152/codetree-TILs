n,m,k=map(int,input().split())
turn=list(map(int,input().split()))
area=[i for i in range(1,m+1)]
max_ap=-99999
#명령을 수행할 말
horse=[]
def move():
    global max_ap
    cnt=0
    #모두 1에서 시작
    start=[1 for _ in range(k)]
    for i in range(n):
        for j in range(turn[i]):
            if start[horse[i]]==m:
                continue
            start[horse[i]]+=1
    max_ap=max(max_ap,start.count(m))
    #print(start)
        
def choose(num):
    if num==n+1:
        #print(horse)
        move()
        return
    for i in range(k):
        horse.append(i)
        choose(num+1)
        horse.pop()
    return
choose(1)
print(max_ap)