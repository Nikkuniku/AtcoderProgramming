n=int(input())
a=list(map(int,input().split()))

def rec(a,m,n,presign,sign):
    if m==n:
        return sign*a[m]
    ans=0
    ans+=rec(a,m+1,n,1,1)
    ans+=rec(a,m+1,n,-1,1) 

    if presign==1:
        ans+=rec(a,m+1,n,1,1)
        ans+=rec(a,m+1,n,1,-1)
        ans+=2*a[m]
    else:
        ans+=rec(a,m+1,n,1,1)
        ans-=a[m]

    return ans

print(rec(a,0,n-1,1,1))
