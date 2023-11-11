a, b, c, d, e, f, x = map(int, input().split())
tak = 0
s = 0
while 1:
    for _ in range(a):
        tak += b
        s += 1
        if s == x:
            break
    if s == x:
        break
    for _ in range(c):
        s += 1
        if s == x:
            break
    if s == x:
        break
aoki = 0
s = 0
while 1:
    for _ in range(d):
        aoki += e
        s += 1
        if s == x:
            break
    if s == x:
        break
    for _ in range(f):
        s += 1
        if s == x:
            break
    if s == x:
        break
ans = 'Takahashi'
if tak == aoki:
    ans = 'Draw'
elif tak < aoki:
    ans = 'Aoki'
print(ans)
