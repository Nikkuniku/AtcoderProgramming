X, Y = map(int, input().split())
ans = max(-(-(Y - X) // 10), 0)
print(ans)
