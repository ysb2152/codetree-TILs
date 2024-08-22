chrs=input()
chrs=list(chrs)
dic={}
for i in range(len(chrs)):
    if chrs[i] not in dic:
        dic[chrs[i]]=1
    else:
        dic[chrs[i]]+=1
for ele in dic:
    if dic[ele]==1:
        print(ele)
        break