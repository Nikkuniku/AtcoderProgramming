n, k = map(int, input().split())
ans = 0
k = str(k)
if len(k) > 1:
    p = int(str(k)[:len(k)//2])
    q = int(str(k)[-(-len(k)//2):][::-1])
else:
    p = int(k)
    q = int(k)
k = int(k)
if p <= q:
    s = set()
    # 1
    x = k
    for _ in range(15):
        if x <= n:
            s.add(x)
        x *= 10
    # 2
    k = int(''.join(list(str(k))[::-1]))
    x = k
    for _ in range(15):
        if x <= n:
            s.add(x)
        x *= 10
    ans = len(s)
print(ans)
