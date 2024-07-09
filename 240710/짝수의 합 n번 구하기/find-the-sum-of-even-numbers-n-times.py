n=int(input())
for _ in range(n):

    a,b=map(int,input().split())
    for i in range(a,b+1):
        cnt=0
        for j in range(a,i+1):
            if j%2==0:
                cnt+=j
    print(f"{cnt}")