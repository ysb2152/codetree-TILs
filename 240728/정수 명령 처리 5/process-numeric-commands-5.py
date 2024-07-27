n=int(input())
L=[]
for i in range(n):
    order=input()
    
    if 'push_back' in order:
        _,num=tuple(order.split())
        num=int(num)
        L.append(num)
        
    if 'pop_back' in order:
        L.pop(len(L)-1)
    if 'size' in order:
        print(len(L))
    if 'get' in order:
        _,num=tuple(order.split())
        num=int(num)
        print(L[num-1])