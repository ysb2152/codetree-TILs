n=int(input())
hashmap={}
lists=[]
max_enc=-9999
for i in range(n):
    chrs=input()
    if chrs not in lists:
        lists.append(chrs)
    if chrs not in hashmap:
        hashmap[chrs]=0
    if chrs in hashmap:
        hashmap[chrs]+=1
for ele in lists:
    max_enc=max(max_enc,hashmap[ele])

print(max_enc)