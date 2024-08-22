n,m=map(int,input().split())
hashmap1={}
hashmap2={}
for i in range(1,n+1):
    chrs=input()
    hashmap1[chrs]=i
    hashmap2[i]=chrs
for i in range(m):
    res=input()
    if res.isdigit():
        res=int(res)
        print(hashmap2[res])
    elif res.isalpha():
        print(hashmap1[res])