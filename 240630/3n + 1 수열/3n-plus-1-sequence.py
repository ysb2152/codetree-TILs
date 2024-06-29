N=int(input())
cnt=0
while True:
    if N%2==0:
        N/=2
        cnt+=1
    elif N%2==1:
        N=(N*3)+1
        cnt+=1
    if N==1:
        print(f"{cnt}")
        break