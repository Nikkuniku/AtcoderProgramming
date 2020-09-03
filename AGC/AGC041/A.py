n,a,b = map(int,input().split())

p = b-a-1

if p%2==0:
    ans=0
    if a <=n-b:
        k = a-1
        a-=k
        b-=(k+1)
        ans+=k+1
    else:
        k = n-b
        a+=(k+1)
        b+=k
        ans += k+1
    p=b-a-1

    print(ans + (p+1)//2)
else:
    print((p+1)//2)