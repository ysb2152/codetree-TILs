n=int(input())
L=[list(map(int,input().split()))for _ in range(n)]
max_cnt=-9999
dxs,dys=[0,1,0,-1],[1,0,-1,0]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def move(a,b,direction):
    cnt=1
    L1=[L[:]for L in L]
    if L1[a][b]==1:
        if direction==0 or direction==2:
            direction=(direction+3)%4
        else:
            direction=(direction+1)%4
    if L1[a][b]==2:
        if direction==0 or direction==2:
            direction=(direction+1)%4
        else:
            direction=(direction+3)%4
    

        

    #L1[a][b]='S'
   
    
    for _ in range(100000):
        #for row in L1:
            #print(row)
        #print(" ")
        new_a,new_b=a+dxs[direction],b+dys[direction]
        #print(new_a,new_b,direction)
        if not in_range(new_a,new_b):
            
            return cnt
        if in_range(new_a,new_b) and L1[new_a][new_b]==0:
            a=new_a
            b=new_b
            #L1[a][b]='S'
            cnt+=1
        if in_range(new_a,new_b) and L1[new_a][new_b]==1:
            if direction==0 or direction==2:
                a=new_a
                b=new_b
                direction=(direction+3)%4
                #L1[a][b]='S'
                cnt+=1
            else:
                a=new_a
                b=new_b
                direction=(direction+1)%4
                #L1[a][b]='S'
                cnt+=1

        if in_range(new_a,new_b) and L1[new_a][new_b]==2:
            if direction==0 or direction==2:
                a=new_a
                b=new_b
                direction=(direction+1)%4
                #L1[a][b]='S'
                cnt+=1
            else:
                a=new_a
                b=new_b
                direction=(direction+3)%4
                #L1[a][b]='S'
                cnt+=1
    return 0

#for i in range(n):
    #print(move(i,n-1,2))
for i in range(n):
    max_cnt=max(max_cnt,move(i,0,0))
    max_cnt=max(max_cnt,move(0,i,1))
    max_cnt=max(max_cnt,move(i,n-1,2))
    max_cnt=max(max_cnt,move(n-1,i,3))
print(max_cnt+1)