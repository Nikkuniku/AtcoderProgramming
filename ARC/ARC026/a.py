N, A, B = map(int, input().split())
ans = min(N, 5) * B
N -= min(N, 5)
ans += N * A
print(ans)
