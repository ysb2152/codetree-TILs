N=int(input())
def comp(a):
    if a==1:
        return 2
    if a==2:
        return 4
    
    return (comp(a-1)*comp(a-2))%100
print(comp(N))