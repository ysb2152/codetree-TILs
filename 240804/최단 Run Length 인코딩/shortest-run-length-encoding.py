a=input()
a=list(a)

min_leng=99999
def record(a):
    
    cnt=0
    for i in range(len(a)):
        if a[0]!=a[i]:
            result.append(a[0])
            result.append(cnt)
            
            return record(a[i:])
        elif cnt==len(a)-1:
            result.append(a[0])
            if cnt>=9:
                result.append((cnt+1)//10)
                result.append((cnt+1)%10)
            else:
                result.append(cnt+1)
            return 0

        else:
            cnt+=1
    
    return 0
def shift(a):
    temp=a[len(a)-1]
    for i in range(len(a)-1,0,-1):
        a[i]=a[i-1]
    a[0]=temp
for i in range(10):
    result=[]
    shift(a)
    record(a)
    
    min_leng=min(min_leng,len(result))


print(min_leng)