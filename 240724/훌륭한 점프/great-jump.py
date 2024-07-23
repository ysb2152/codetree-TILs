n,k=map(int,input().split())
arr=list(map(int,input().split()))

def is_possible(max_val,k):
    available_indices = []
    for i, elem in enumerate(arr):
        if elem <= max_val:
            available_indices.append(i)
    
        

    arr_size = len(available_indices)
    
    if arr_size==1:
        
        return False
    for i in range(1, arr_size):
        dist = available_indices[i] - available_indices[i - 1]
       
        if dist > k:
            return False
    
    
    return True
minmax = 999999
for a in range(max(arr),min(arr)-1,-1):
    if is_possible(a,k):
        minmax = min(minmax, a)

print(minmax)