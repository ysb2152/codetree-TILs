N=int(input())
cnt=0
while True:
    if N%2==0:
        cnt+=1
        N/=2
    else:
        print(f"{cnt}")
        break