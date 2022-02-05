n=int(input())
a=list(map(int,input().split()))


def eur(A,B):
    while A>=1 and B>=1:
        if B>A:
            B=B%A
        else:
            A=A%B
    if A>=1:
        return A
    else:
        return B

ans=a[0]
for i in range(n-1):
    ans = eur(ans,a[i+1])

print(ans)