n=int(input())
hashmap={}
for i in range(n):
    order=input()
    if order.startswith('add'):
        
        order,key,value=order.split()
        hashmap[key]=value
    if order.startswith('remove'):
        order,key=order.split()
        hashmap.pop(key)
    if order.startswith('find'):
        order,key=order.split()
        if key in hashmap:
            print(hashmap[key])
        else:
            print("None")