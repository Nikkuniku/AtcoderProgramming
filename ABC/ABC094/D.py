n=int(input())
a=list(map(int,input().split()))

a=sorted(a)


b=a.pop(-1)
mid=b/2
dist=10**9
for i in range(n-1):

    #できるだけ最大値から離れた値
    d=abs(mid-a[i])
    if d <dist:
        dist=d
        ans=a[i]

print(b,ans)

