a,b,c=map(int,input().split())
s=False

for i in range(a,b+1):
    if i%c==0:
        s=True

if s==True:
    print("NO")
else:
    print("YES")