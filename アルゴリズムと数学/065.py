h,w=map(int,input().split())
a=w-w//2
b=w//2

c=h-h//2
d=h//2

ans=a*c + b*d
if h==1 or w==1:
    ans=1 
print(ans)