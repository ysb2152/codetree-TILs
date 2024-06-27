n=list(map(int,input().split()))
n.remove(min(n))
n.remove(max(n))
print(n[0])