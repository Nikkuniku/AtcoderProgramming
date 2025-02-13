N = int(input())
H = list(map(int, input().split()))
INF = 1 << 60
stack = [(INF, 0)]
cum = [0]
for i, h in enumerate(H, start=1):
    while stack[-1][0] < h:
        stack.pop()
    v, j = stack[-1]
    tmp = cum[j] + h * (i - j)
    cum.append(tmp)
    stack.append((h, i))
ans = [cum[i] + 1 for i in range(1, N + 1)]
print(*ans)
