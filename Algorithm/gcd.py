a,b=map(int,input().split())

def gcd(m,n):
    if n==0:
        return m

    return gcd(n,m%n)

print(gcd(a,b))