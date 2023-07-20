r, g, b = map(int, input().split())
ans = 'NO'
if (10*g+b) % 4 == 0:
    ans = 'YES'
print(ans)
