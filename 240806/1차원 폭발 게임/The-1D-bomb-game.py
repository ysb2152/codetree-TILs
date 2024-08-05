n,m=map(int,input().split())
L=[int(input()) for _ in range(n)]
def check():
    global L
    cnt=1
    
    if len(L)==0 and m==1:
        return False
    if len(L)==1 and len(L)==0:
        return False
    if len(L)==1 and m==1:
        L=[]
        return False
    
    for i in range(len(L)-1,0,-1):
       
        if L[i]==L[i-1]:
            cnt+=1
            
       
        else:
            if cnt>=m:
                
                return True
            cnt=1
    if cnt==m and len(L)==m:
        L=[]
        return False
    return False
        
    
def explode():
    global L
    cnt=1
    
    if len(L)==1 and len(L)==0:
        return 0
    for i in range(len(L)-1,0,-1):
       
        if L[i]==L[i-1]:
            cnt+=1
       
        else:
            if cnt>=m:
                for j in range(i+(cnt-1),i-1,-1):
                    L[j]=0
            if cnt==m and len(L)==m:
                L=[0 for _ in range(m)]
            cnt=1
    
    
        
   
def remove0():
    global L
    temp=[]
    for i in range(len(L)):
        if L[i]!=0:
            temp.append(L[i])
    L=temp
while check():
    
    explode()
    remove0()
    
   
if len(L)==0:
    print("0")
else:
    print(len(L))
    for ele in L:
        print(ele)