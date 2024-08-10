line=input()
line=list(line)
max_ans=-9999999
alphas=[]
nums=[]
for ele in line:
    if ele.isalpha()==True and ele not in alphas:
        alphas.append(ele)

def choose(num):
    if num==len(alphas)+1:
        calculate()
        return
    for i in range(1,5):
        nums.append(i)
        choose(num+1)
        nums.pop()
    return
def calculate():
    
    global max_ans
    lines=[line[:]for line in line]
    
    for j in range(len(lines)):
        if lines[j].isalpha()==True and lines[j] in alphas:
            lines[j]=nums[alphas.index(lines[j])]
     
    
    while len(lines)!=1:
        if lines[1].isdigit()==False:
            if lines[1]=='+':
                a=lines[0]+lines[2]
                new_lines=[a]
                if len(lines)>3:
                    for k in range(3,len(lines)):
                        new_lines.append(lines[k])
                lines=new_lines
                continue
            if lines[1]=='-':
                a=lines[0]-lines[2]
                new_lines=[a]
                if len(lines)>3:
                    for k in range(3,len(lines)):
                        new_lines.append(lines[k])
                lines=new_lines
                continue
            if lines[1]=='*':
                a=lines[0]*lines[2]
                new_lines=[a]
                if len(lines)>3:
                    for k in range(3,len(lines)):
                        new_lines.append(lines[k])
                lines=new_lines
                continue
    
    max_ans=max(max_ans,lines[0])
choose(1)
print(max_ans)