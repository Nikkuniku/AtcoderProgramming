x, y, z = map(int, input().split())

ans = -1
if x*y < 0:
    ans = abs(x)
else:
    if 0 < y < x:
        if z < y:
            ans = abs(z)+abs(y-z)+abs(x-y)
    elif x < y < 0:
        if y < z:
            ans = abs(z)+abs(y-z)+abs(x-y)
    elif 0 < x < y:
        ans = abs(x)
    elif y < x < 0:
        ans = abs(x)
print(ans)
