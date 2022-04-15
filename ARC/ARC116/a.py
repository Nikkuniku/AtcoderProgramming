t=int(input())
for _ in range(t):
    c=int(input())
    ans='Same'
    if c%2==1:
        ans='Odd'
    else:
        if c%4==0:
            ans='Even'

    print(ans)


def binomial(n,r):
    re=1
    for i in range(1,n+1):
        re*=i
    for j in range(1,r+1):
        re//=j
        re//=(n-j)
    return re

n=3
for i in range(n+1):
    print(binomial(n,i))