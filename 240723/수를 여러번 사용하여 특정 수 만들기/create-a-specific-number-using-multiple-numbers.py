A,B,C=map(int,input().split())
max_compA=C//A
max_compB=C//B
max_makeC=0
for i in range(max_compA):
    mul=0
    for j in range(max_compB):
        mul=i*A+j*B
        if mul>C:
            continue
        
        max_makeC=max(max_makeC,mul)
print(max_makeC)