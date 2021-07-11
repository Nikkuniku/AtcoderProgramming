n=int(input())

n-=2

ans=0
if n<0:
    ans=0
elif n==0:
    ans=1
else:
    ans=n+1

print(ans)
