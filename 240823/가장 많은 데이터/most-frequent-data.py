n=int(input())
hashmap={}

max_enc=-9999
for i in range(n):
    chrs=input()
    
    if chrs not in hashmap:
        hashmap[chrs]=0
    if chrs in hashmap:
        hashmap[chrs]+=1
for ele in hashmap:
    max_enc=max(max_enc,hashmap[ele])

print(max_enc)