n=int(input())
L=list(map(int,input().split()))


def partition(low, high):
  pivot = L[high]
  i = low - 1
  
  for j in range(low,high):
    if L[j] < pivot:
      i += 1
      
      a=L[i]
      L[i]=L[j]
      L[j]=a
      
  
  b=L[i+1]
  L[i+1]=L[high]
  L[high]=b
  return i + 1

def quick_sort(low, high):
  if low < high:
    pos = partition(low, high)
    
    quick_sort(low, pos - 1)
    quick_sort(pos + 1, high)
quick_sort(0,n-1)
for ele in L:
  print(ele,end=" ")