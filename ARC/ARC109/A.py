a,b,x,y=map(int,input().split())

ans=0
if a<=b:
    ans=min(y*(b-a) + x,x + 2*x*(b-a))
else:
    ans=x + min(y*(a-b-1),2*x*(a-b-1))

print(ans) 