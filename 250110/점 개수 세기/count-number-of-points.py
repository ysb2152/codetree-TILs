n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]
points.sort()
def find_min(num):
    left=0
    right=n-1
    max_val=-1
    while left<=right:
        mid=(left+right)//2
        if points[mid]<=num:
            max_val=max(max_val,mid)
            left=mid+1
        else:
            right=mid-1
    return max_val
def find_max(num):
    left=0
    right=n-1
    min_val=n 
    while left<=right:
        mid=(left+right)//2
        if points[mid]>=num:
            min_val=min(min_val,mid)
            right=mid-1
        else:
            left=mid+1
    return min_val
for i in range(len(queries)):
    a,b=queries[i]
    print(find_min(b)-find_max(a)+1)
# Write your code here!
