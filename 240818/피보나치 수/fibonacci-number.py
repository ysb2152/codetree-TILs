n=int(input())
table=[-1 for _ in range(n+1)]
table[0]=1
table[1]=1
def fibbo(n):
    global table
    if table[n]!=-1:
        return table[n]
    if n<=2:
        table[n]=1
    else:
        table[n]=fibbo(n-1)+fibbo(n-2)
    return table[n]
print(fibbo(n))