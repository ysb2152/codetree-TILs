c=input()
b=c
cnt=0
cnt1=0
for i in range(20):
    if 'ee' in c:
        cnt+=1
        c=c[c.find('ee')+1:]
        
        
    else:
        break
for i in range(20):
    if 'eb' in b:
        cnt1+=1
        b=b[b.find('eb')+1:]
        
    else:
        break
print(cnt,end=" ")
print(cnt1)