c=input()
n=int(input())
if n>=(len(c)):
    c=c[::-1]
else:
    c=c[:-n-1:-1]
print(c)