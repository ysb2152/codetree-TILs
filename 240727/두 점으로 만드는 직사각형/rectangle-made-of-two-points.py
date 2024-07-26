x1,y1,x2,y2=map(int,input().split())
a1,b1,a2,b2=map(int,input().split())
xlayer=[x1,x2,a1,a2]
ylayer=[y1,y2,b1,b2]
print((max(xlayer)-min(xlayer))*(max(ylayer)-min(ylayer)))