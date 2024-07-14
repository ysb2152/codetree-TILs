def game(n):
    n=list(str(n))
    
    for ele in n:
        if '3' in n or '6' in n or '9' in n:
            return 1
        else:
            return 0
def ismul(n):
    if n%3==0:
        return 1
    else:
        return 0
a,b=map(int,input().split())
cnt=0
for i in range(a,b+1):
    if (int(game(i))+int(ismul(i)))>=1:
        
        cnt+=1
print(cnt)