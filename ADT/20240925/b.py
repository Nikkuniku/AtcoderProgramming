H, W = map(int, input().split())
ans = 0
for _ in range(H):
    S = input()
    ans += S.count("#")
print(ans)
