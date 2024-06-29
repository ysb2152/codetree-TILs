n=int(input())
s=False
cnt=0
for i in range(1,n+1):
    if n%i==0:
        s=True
        cnt+=1

if cnt>=3:
    print("C")
else:
    print("P")