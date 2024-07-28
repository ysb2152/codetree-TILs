n=int(input())
L=list(map(int,input().split()))

merged_arr=[0 for _ in range(n)]
def merge(low,mid,high):
    i,j=low,mid+1
    k=low
    while i<=mid and j<=high:
        if L[i]<=L[j]:
            merged_arr[k]=L[i]
            k+=1
            i+=1
        else:
            merged_arr[k]=L[j]
            k+=1
            j+=1
    while i<=mid:
        merged_arr[k]=L[i]
        k+=1
        i+=1
    while j<=high:
        merged_arr[k]=L[j]
        k+=1
        j+=1
    for k in range(low,high+1):
        L[k]=merged_arr[k]
    
def merge_sort(low,high):
    if low<high:
        mid=(low+high)//2
        merge_sort(low,mid)
        merge_sort(mid+1,high)
        merge(low,mid,high)
merge_sort(0,n-1)
for ele in L:
    print(ele,end=" ")