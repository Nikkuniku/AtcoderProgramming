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

n=int(input())
a=list(map(int,input().split()))

ans=1
for i in range(n):
    ans=(ans*a[i])//eur(ans,a[i])

print(ans)