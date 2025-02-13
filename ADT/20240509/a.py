N = int(input())
X, Y = 0, 0
for _ in range(N):
    a, b = map(int, input().split())
    X += a
    Y += b
ans = "Draw"
if X > Y:
    ans = "Takahashi"
elif X < Y:
    ans = "Aoki"
print(ans)
