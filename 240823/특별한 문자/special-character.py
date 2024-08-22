chrs=input()
chrs=list(chrs)
dic={}
cntlist=[]
for i in range(len(chrs)):
    if chrs[i] not in dic:
        dic[chrs[i]]=1
    else:
        dic[chrs[i]]+=1
for ele in dic:
    if dic[ele]==1:
        print(ele)
        break
    else:
        cntlist.append(ele)

if len(dic)==len(cntlist):
    print("None")