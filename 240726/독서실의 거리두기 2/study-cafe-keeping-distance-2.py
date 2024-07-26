n=int(input())
L=input()
L=list(L)
comp=[]
for i in range(n):
    cnt=0
    
    for j in range(i+1,n):
        if L[i]=='1'and L[j]=='1':
            comp.append([i,j,j-i])
            break

comp.sort(key=lambda x:x[2])
L[comp[len(comp)-1][0]+(comp[len(comp)-1][2]//2)]='1'
max_cnt=99999

for i in range(n):
    cnt=0
    
    for j in range(i+1,n):
        if L[i]=='1'and L[j]=='1':
            cnt=j-i
            
            min_cnt=min(max_cnt,cnt)
            break
print(min_cnt)