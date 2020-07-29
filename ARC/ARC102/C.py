n,k=map(int,input().split())

ans=0
if k%2==0:
    cnt=0
    k_d = k//2

    for i in range(n+1):
        if i%k==k_d:
            cnt+=1

    x=n//k
    ans+=(x**3) +(cnt**3)
else:
    x=n//k
    ans+=x**3

print(ans)