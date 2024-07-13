n,A=input().split()
n=int(n)
cnt=0
for _ in range(n):
    c=input()
    if c==A:
        cnt+=1
print(cnt)