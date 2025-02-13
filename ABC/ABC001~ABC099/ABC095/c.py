A, B, C, X, Y = map(int, input().split())
ans = 1 << 60
for i in range(2 * max(X, Y) + 1):
    cost_a = max(X - i // 2, 0) * A
    cost_b = max(Y - i // 2, 0) * B
    cost_c = i * C
    ans = min(ans, cost_a + cost_b + cost_c)
print(ans)
