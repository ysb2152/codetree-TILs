n=int(input())
cnt=0
for _ in range(n):
    c=int(input())
    cnt+=c
cnt=str(cnt)
cnt=cnt[1:]+cnt[0]
print(cnt)