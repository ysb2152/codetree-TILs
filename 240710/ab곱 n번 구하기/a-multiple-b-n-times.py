n=int(input())
for _ in range(n):
    arr=input().split()
    a,b=int(arr[0]),int(arr[1])
    
    mul=1
    for i in range(a,b+1):
        mul*=i
    print(f"{mul}")