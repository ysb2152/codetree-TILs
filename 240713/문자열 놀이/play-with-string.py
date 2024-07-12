s,q=input().split()
q=int(q)
t=list(s)

for _ in range(q):
    L=input().split()
    
    if L[0]=='1':
        a=t[int(L[1])-1]
        
        t[int(L[1])-1]=t[int(L[2])-1]
        t[int(L[2])-1]=a
        t=''.join(t)
        print(t)
        t=list(t)
        continue
    if L[0]=='2':
        for i in range(0,len(t)):
            if t[i]==L[1]:
                t[i]=L[2]
            t=''.join(t)
            if L[1] not in t:
                print(t)
            t=list(t)