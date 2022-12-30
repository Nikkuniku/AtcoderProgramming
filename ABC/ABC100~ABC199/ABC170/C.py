x,n=map(int,input().split())
p=list(map(int,input().split()))

if n==0:
    print(x)
    exit(0)

p=sorted(p)

dist=10*9
ans=102
for i in range(102,-2,-1):
    if abs(x-i)<=dist and i not in p:
        dist = abs(x-i)
        ans = i
        if i<=ans:
            ans = i
        

print(ans)


