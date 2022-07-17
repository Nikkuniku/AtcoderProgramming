x, y, a, b = map(int, input().split())
ans = 0
while True:
    if x+b <= min(a*x, y-1):
        k = (min(a*x, y-1)-x)//b
        if k > 0:
            x += k*b
            ans += k
    else:
        if a*x < y:
            x *= a
            ans += 1
        else:
            break
print(ans)
