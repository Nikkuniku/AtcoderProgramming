a,b,c,k = map(int,input().split())

d={}

d[1]=a
d[0]=b
d[-1]=c

ans = 0
cnt=0

cnt+=a
ans+=a
if cnt>k:
    ans-=(cnt-k)
    print(ans)
    exit(0)

cnt+=b
if cnt>k:
    print(ans)
    exit(0)

cnt+=c
ans-=c
if cnt>k:
    ans+=(cnt-k)
    print(ans)
    exit(0)

if cnt==k:
    print(ans)