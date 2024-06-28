n=int(input())
numm=0
for i in range(1,n):
    if n%i==0:
        
        numm+=i
if numm==n:
    print("P")
else:
    print("N")