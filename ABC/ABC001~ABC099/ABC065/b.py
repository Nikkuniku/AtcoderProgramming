n = int(input())
a = [int(input())-1 for _ in range(n)]
ans = 0
i = 0
ok = False
for _ in range(n):
    i = a[i]
    ans += 1
    if i == 1:
        ok = True
        break

if ok:
    print(ans)
else:
    print(-1)
