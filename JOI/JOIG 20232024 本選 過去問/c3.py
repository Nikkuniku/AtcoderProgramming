N = int(input())
left = [-1] * N
right = [N] * N
V = []
for i in range(N):
    c, x = map(int, input().split())
    V.append((i, c, x))
V.sort(key=lambda x: x[2])
for i in range(1, N):
    if V[i - 1][1] != V[i][1]:
        left[i] = i - 1
    else:
        left[i] = left[i - 1]
for i in range(N - 2, -1, -1):
    if V[i][1] != V[i + 1][1]:
        right[i] = i + 1
    else:
        right[i] = right[i + 1]
ans = [1 << 60] * N
for j in range(N):
    i, _, x = V[j]
    if left[j] != -1:
        ans[i] = min(ans[i], x - V[left[j]][2])
    if right[j] != N:
        ans[i] = min(ans[i], V[right[j]][2] - x)
print(*ans, sep="\n")
