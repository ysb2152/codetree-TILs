A=input()
B=[]
c=1
cnt=0
if len(A)==1:
    B.append(A)
    B.append(c)

for i in range(0,len(A)-1):
    if c==1:
        
        B.append(A[i])
    if A[i]==A[i+1]:
        if i==len(A)-2:
            B.append(c+1)
            
        
        c+=1
    else:
        
        B.append(c)
        c=1
        if i==len(A)-2:
            B.append(A[i+1])
            B.append(1)
for ele in B:
    if type(ele)==int and ele>=10:
        cnt+=1
    if type(ele)==int and ele>=100:
        cnt+=2
        
    else:
        cnt+=1
print(cnt)  
       
for ele in B:
    print(ele,end="")