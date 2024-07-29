n=int(input())
L=[0]+list(map(int,input().split()))
def heapify(n, i):
  largest = i
  l = i * 2
  r = i * 2 + 1

  if l <= n and L[l] > L[largest]:
    largest = l

  if r <= n and L[r] > L[largest]:
    largest = r

  if largest != i:
    
    a=L[i]
    L[i]=L[largest]
    L[largest]=a
    heapify(n, largest)

def heap_sort(n):
  for i in range((n//2),0,-1):
    heapify(n, i)

  for i in range(n,1,-1):
    
    a=L[1]
    L[1]=L[i]
    L[i]=a
    heapify(i - 1, 1)
heap_sort(n)
for ele in L[1:]:
    print(ele,end=" ")