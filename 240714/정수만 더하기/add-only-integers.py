A=input()
A=list(A)
cnt=0
for ele in A:
    if ele.isdigit()==True:
        cnt+=int(ele)
print(cnt)