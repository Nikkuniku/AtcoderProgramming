n,k,a=map(int,input().split())

b=k%n -1

ans=a+b+1 if k%n==0 else a+b

if ans>=n+1:
    ans-=a

print(ans)