t=int(input())
dxs,dys=[-1,1,0,0],[0,0,1,-1]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
for _ in range(t):
    cnt=0
    n,m=map(int,input().split())
    L=[[0 for _ in range(n)]for _ in range(n)]
    dir_L=[[0 for _ in range(n)]for _ in range(n)]
    for _ in range(m):
        x,y,d=input().split()
        x=int(x)-1
        y=int(y)-1
                
        dir_L[x][y]=d
        L[x][y]=1
    #for row in dir_L:
        #print(row)
    #print(" ")
    for time in range(100000):
        new_L=[[0 for _ in range(n)]for _ in range(n)]
        new_dir_L=[[0 for _ in range(n)]for _ in range(n)]
        #for row in L:
            #print(row)
        #print(" ")
        #for row in dir_L:
            #print(row)
        #print(" ")
        for i in range(n):
            for j in range(n):
                if L[i][j]==1:
                    
                    if dir_L[i][j]=='U':
                        new_i,new_j=i+dxs[0],j+dys[0]
                        if not in_range(new_i,new_j):
                            new_L[i][j]+=1
                            new_dir_L[i][j]='D'
                            continue
                        else:
                                                        
                            new_L[new_i][new_j]+=1
                            new_dir_L[new_i][new_j]='U'
                            continue
                    if dir_L[i][j]=='D':
                        new_i,new_j=i+dxs[1],j+dys[1]
                        if not in_range(new_i,new_j):
                            new_L[i][j]+=1
                            new_dir_L[i][j]='U'
                            continue
                        else:
                            
                            
                            new_L[new_i][new_j]+=1
                            new_dir_L[new_i][new_j]='D'
                            continue
                    if dir_L[i][j]=='R':
                        new_i,new_j=i+dxs[2],j+dys[2]
                        
                        if not in_range(new_i,new_j):
                            
                            new_L[i][j]+=1
                            new_dir_L[i][j]='L'
                            
                            continue
                        else:
                            
                            
                            new_L[new_i][new_j]+=1
                            new_dir_L[new_i][new_j]='R'
                            continue
                    if dir_L[i][j]=='L':
                        new_i,new_j=i+dxs[3],j+dys[3]
                        if not in_range(new_i,new_j):
                            new_L[i][j]+=1
                            new_dir_L[i][j]='R'
                            continue
                        else:
                                                        
                            new_L[new_i][new_j]+=1
                            new_dir_L[new_i][new_j]='L'
                            continue
                    
                #for row in new_dir_L:
                    #print(row)
                #print(" ")
                    #for row in new_L:
                        #print(row)
                    #print(" ")
        for k in range(n):
            for L in range(n):
                if new_L[k][L]>1:
                    new_L[k][L]=0
        L=new_L
        dir_L=new_dir_L
    for row in L:
        for ele in row:
            if ele==1:
                cnt+=1
    print(cnt)