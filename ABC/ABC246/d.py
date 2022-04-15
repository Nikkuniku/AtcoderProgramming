n=int(input())

ans=10**18
def func(a,b):
    return pow(a,3)+pow(a,2)*b+a*pow(b,2)+pow(b,3)

for a in range(pow(10,6)+1):
    l=-1
    r=pow(10,6)+1
    while r-l>1:
        mid=(l+r)//2
        if func(a,mid)>=n:
            r=mid
        else:
            l=mid
    
    ans=min(ans,func(a,r))

print(ans)
