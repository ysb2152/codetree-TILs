import sys
n=int(input())
L=list(map(int,input().split()))
max_cnt=-sys.maxsize

for i in range(n):
    cnt=0
    for j in range(i+1,n):
        for k in range(j+1,n):
            if L[i]>0 and L[j]>0 and L[k]>0:
                cnt=L[i]*L[j]*L[k]
                max_cnt=max(max_cnt,cnt)
            if L[i]*L[j]>0 and L[k]>0:
                cnt=L[i]*L[j]*L[k]
                max_cnt=max(max_cnt,cnt)
            if L[i]*L[j]<0 and L[k]<0:
                cnt=L[i]*L[j]*L[k]
                max_cnt=max(max_cnt,cnt)
            if L[i]*L[k]>0 and L[j]>0:
                cnt=L[i]*L[j]*L[k]
                max_cnt=max(max_cnt,cnt)
            if L[i]*L[k]<0 and L[j]<0:
                cnt=L[i]*L[j]*L[k]
                max_cnt=max(max_cnt,cnt)
            if L[j]*L[k]>0 and L[i]>0:
                cnt=L[i]*L[j]*L[k]
                max_cnt=max(max_cnt,cnt)
            if L[j]*L[k]<0 and L[i]<0:
                cnt=L[i]*L[j]*L[k]
                max_cnt=max(max_cnt,cnt)
            if L[i]<0 and L[j]<0 and L[k]<0:
                cnt=L[i]*L[j]*L[k]
                max_cnt=max(max_cnt,cnt)
            if L[i]==0 or L[j]==0 or L[k]==0:
                cnt=0
                max_cnt=max(max_cnt,cnt)
print(max_cnt)