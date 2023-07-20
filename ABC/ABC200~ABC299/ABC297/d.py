from math import gcd

A, B = map(int, input().split())
g = gcd(A, B)
ans = 0
while A != B:
    if A > B:
        if B > g:
            ans += A//B
            A = A % B
        else:
            ans += (A-g)//g
            A = g
    elif A < B:
        if A > g:
            ans += B//A
            B = B % A
        else:
            ans += (B-g)//g
            B = g

print(ans)
