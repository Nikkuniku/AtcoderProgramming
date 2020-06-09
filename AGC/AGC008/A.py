x,y=map(int,input().split())

ans =0

if 0<x and x<y:
    ans=abs(y) - abs(x)
elif x==-y:
    ans =1
elif x==0 and x<y:
    ans =abs(y) - abs(x)    
elif x<0 and 0<y and (abs(x) < abs(y)):
    ans = 1 + abs(y) - abs(x)
elif x<0 and 0<y and (abs(x) > abs(y)):
    ans = 1 + abs(x) - abs(y)
elif x<y and y<0:
    ans = abs(x) - abs(y)
elif x<y and y==0:
    ans = abs(x) - abs(y)
elif 0<y and y<x:
    ans = 2 + abs(x) - abs(y)
elif y==0 and y<x:
    ans = 1 + abs(x) - abs(y)
elif y<0 and 0<x and (abs(x) > abs(y)):
    ans = 1 + abs(x) - abs(y)
elif y<0 and 0<x and (abs(x) < abs(y)):
    ans = 1 + abs(y) - abs(x)
elif y<x and x<0:
    ans = 2 + abs(y) - abs(x)
elif y<x and x==0:
    ans = 1 + abs(y)
print(ans)
