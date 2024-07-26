L=list(map(int,input().split()))
cnt=0
while True:

    if L[0]+1==L[1] and L[1]+1==L[2]:
        break
    if abs(L[1]-L[0])>abs(L[1]-L[2]):
        L[2]=L[1]
        L[1]=L[1]-1
    elif abs(L[1]-L[0])<abs(L[1]-L[2]):
        L[0]=L[1]
        L[1]=L[2]-1
    cnt+=1
print(cnt)