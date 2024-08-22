chrs=input()
chrs=list(chrs)
dic={}
cnt=0
for i in range(len(chrs)):
    if chrs[i] not in dic:
        dic[chrs[i]]=1
    else:
        dic[chrs[i]]+=1
for ele in dic:
    if dic[ele]==1:
        print(ele)
        break
    cnt=1
if cnt==1:
    print("None")