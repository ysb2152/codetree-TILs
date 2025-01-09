n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]
dic={}
for i in range(len(points)):
    dic[points[i]]=i 
for i in range(len(queries)):
    a,b=queries[i]
    print(dic[b]-dic[a]+1)
# Write your code here!
