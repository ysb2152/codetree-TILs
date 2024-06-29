i=0
prod=0
cnt=0
while True:
    i=int(input())
    
    if i>=30 or i<20:
        break
    prod+=i
    cnt+=1
    
print(f"{prod/cnt:.2f}")