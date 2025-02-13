N, M = map(int, input().split())
H = list(map(int, input().split()))
ans = 0
for h in H:
    if h <= M:
        ans += 1
        M -= h
    else:
        M -= h
print(ans)
