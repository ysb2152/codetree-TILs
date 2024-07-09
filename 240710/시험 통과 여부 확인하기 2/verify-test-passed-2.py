n=int(input())
cnt=0
for _ in range(n):
    
    L=list(map(int,input().split()))
    if (sum(L)/len(L))>=60:
        print("pass")
        cnt+=1
    else:
        print("fail")
print(cnt)