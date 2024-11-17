n=int(input())
cnt=1
c=n
a=c//10
b=c%10  
j=a+b
c=b*10+(j%10)
while c!=n:
    a=c//10
    b=c%10  
    j=a+b
    c=b*10+(j%10)
    #print(c)
    cnt+=1
print(cnt)
