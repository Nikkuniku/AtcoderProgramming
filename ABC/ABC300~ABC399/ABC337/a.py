N = int(input())
t = 0
a = 0
for _ in range(N):
    x, y = map(int, input().split())
    t += x
    a += y
ans = "Takahashi"
if t == a:
    ans = "Draw"
elif t < a:
    ans = "Aoki"
print(ans)
