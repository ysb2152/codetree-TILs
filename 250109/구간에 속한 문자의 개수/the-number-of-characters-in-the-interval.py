n, m, k = map(int, input().split())

# Read grid as list of strings since we need character-by-character access
grid = [input() for _ in range(n)]
grid=[[0 for _ in range(m)]]+grid
#for ele in grid:
    #print(ele)
# Read k queries as tuples
queries = [list(map(int, input().split())) for _ in range(k)]

# Write your code here!
grida=[]
gridb=[]
gridc=[]
for ele in grid:
    temp=[0]
    
    for i in range(len(ele)):
        if ele[i]=='a':
            temp.append(1)
        else:
            temp.append(0)
    grida.append(temp)
for ele in grid:
    temp=[0]
    
    for i in range(len(ele)):
        if ele[i]=='b':
            temp.append(1)
        else:
            temp.append(0)
    gridb.append(temp)
for ele in grid:
    temp=[0]
    
    for i in range(len(ele)):
        if ele[i]=='c':
            temp.append(1)
        else:
            temp.append(0)
    gridc.append(temp)
prefixa=[[0 for _ in range(m+1)]for _ in range(n+1)]
prefixb=[[0 for _ in range(m+1)]for _ in range(n+1)]
prefixc=[[0 for _ in range(m+1)]for _ in range(n+1)]
#for ele in grida:
    #print(ele)
#print(" ")
#for ele in prefixa:
    #print(ele)
for i in range(1,n+1):
    for j in range(1,m+1):
        prefixa[i][j]=prefixa[i-1][j]+prefixa[i][j-1]-prefixa[i-1][j-1]+grida[i][j]
for i in range(1,n+1):
    for j in range(1,m+1):
        prefixb[i][j]=prefixb[i-1][j]+prefixb[i][j-1]-prefixb[i-1][j-1]+gridb[i][j]
for i in range(1,n+1):
    for j in range(1,m+1):
        prefixc[i][j]=prefixc[i-1][j]+prefixc[i][j-1]-prefixc[i-1][j-1]+gridc[i][j]
#for ele in prefixa:
    #print(ele)
for ele in queries:
    cnta=0
    cntb=0
    cntc=0
    r1,c1,r2,c2=ele[0],ele[1],ele[2],ele[3]
    cnta=prefixa[r2][c2]-prefixa[r1-1][c2]-prefixa[r2][c1-1]+prefixa[r1-1][c1-1]
    cntb=prefixb[r2][c2]-prefixb[r1-1][c2]-prefixb[r2][c1-1]+prefixb[r1-1][c1-1]
    cntc=prefixc[r2][c2]-prefixc[r1-1][c2]-prefixc[r2][c1-1]+prefixc[r1-1][c1-1]
    print(cnta,cntb,cntc)
