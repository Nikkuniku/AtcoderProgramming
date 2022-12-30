a, b, c, d, e, f, x = map(int, input().split())

takahashi = (x//(a+c))*a*b
aoki = (x//(d+f))*d*e
p = x % (a+c)
if p > a:
    takahashi += a*b
else:
    takahashi += p*b
q = x % (d+f)
if q > d:
    aoki += d*e
else:
    aoki += q*e

ans = 'Draw'
if takahashi > aoki:
    ans = 'Takahashi'
elif takahashi < aoki:
    ans = 'Aoki'
print(ans)
