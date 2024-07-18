N,K,P,T=map(int,input().split())
info=[]
Shake=[[]for _ in range(N)]
infect=[0 for _ in range(N)]

for i in range(T):
    t,x,y=map(int,input().split())
    info.append([t,x,y])
info.sort()

for i in range(len(info)):
    Shake[info[i][1]].append(info[i][2])

for i in range(N):
    if i==P:
        if K==0:
            break
        infect[i]==1
        
        for ele in Shake[i]:
            
            infect[ele-1]=1
            K-=1
infect[P-1]=1
for ele in infect:
    print(ele,end="")