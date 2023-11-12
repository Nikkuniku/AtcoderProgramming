N, X = map(int, input().split())
ans = 0
S = list(map(int, input().split()))
for s in S:
    if s <= X:
        ans += s
print(ans)
