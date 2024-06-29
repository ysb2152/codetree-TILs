i=0
cnt=0
while True:
    i=int(input())
    if i%2==0:
        print(f"{i//2}")
        cnt+=1
    if cnt==3:
        break