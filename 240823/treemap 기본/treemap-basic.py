from sortedcontainers import SortedDict
n=int(input())
sd=SortedDict()
for i in range(n):
    a=input()
    if a.startswith('add'):
        _,k,v=a.split()
        k,v=int(k),int(v)
        sd[k]=v
    if a.startswith('remove'):
        _,k=a.split()
        k=int(k)
        sd.pop(k)
    if a.startswith('find'):
        _,k=a.split()
        k=int(k)
        if k in sd:
            print(sd[k])
        else:
            print("None")
    if a.startswith('print_list'):
        if len(sd)==0:
            print("None")
        else:
            
            for k,v in sd.items():
                print(v,end=" ")
            print(" ")