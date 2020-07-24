n=int(input())
a=list(map(int,input().split()))

a=sorted(a)
a=list(reversed(a))
ans=0

for i in range(2*n):
    if i%2==1:
        ans+=a[i]

print(ans)
