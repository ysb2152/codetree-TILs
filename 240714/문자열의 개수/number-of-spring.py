cnt=0
L=[]
for _ in range(200):
    c=input()
    if c=='0':
        
        break
    cnt+=1
    if cnt%2==1:
        L.append(c)
print(cnt)
for ele in L:
    print(ele)