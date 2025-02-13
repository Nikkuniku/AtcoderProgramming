X, Y = map(int, input().split())
ans = (max(Y - X, 0) + 9) // 10
print(ans)
