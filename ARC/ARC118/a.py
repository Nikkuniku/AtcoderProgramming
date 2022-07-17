t, n = map(int, input().split())

for r in range(100):
    if (100*n + r) % t == 0:
        a = (100*n + r)//t
        break

ans = a+n-1
print(ans)
