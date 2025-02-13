sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
p = abs(ty - sy)
ans = p
if sy % 2 != 0:
    if sx % 2 == 0:
        b = sx + p
        a = sx - 1 - p
    else:
        a = sx - p
        b = sx + 1 + p
else:
    if sx % 2 == 0:
        b = sx + 1 + p
        a = sx - p
    else:
        a = sx - 1 - p
        b = sx + p
if a <= tx <= b:
    exit(print(ans))
if ty % 2 != 0:
    ka = (a + 1) // 2
    kb = (b + 1) // 2
    ktx = (tx + 1) // 2
else:
    ka = (a + 2) // 2
    kb = (b + 2) // 2
    ktx = (tx + 2) // 2
q = min(abs(ka - ktx), abs(kb - ktx))
ans += q
print(ans)
