n=int(input())
def rect(n):
 k=1
 for _ in range(n):
  for i in range(n):
      if i>=n-1:
        print(f"{k}")
      else:
       print(f"{k} ",end="")
      k+=1
      if k>9:
       k=1
      
rect(n)