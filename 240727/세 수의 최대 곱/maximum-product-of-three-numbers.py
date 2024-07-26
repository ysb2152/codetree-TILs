import sys
n=int(input())
L=list(map(int,input().split()))
max_cnt=-sys.maxsize
L.sort()
max1=L[-1]*L[-2]*L[-3]
max2=L[0]*L[1]*L[-1]
print(max(max1,max2))