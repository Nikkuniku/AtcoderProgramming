N, D = map(int, input().split())
if N * D > N * (N - 1) // 2:
    exit(print("No"))
ans = []
for i in range(N):
    for j in range(D):
        if i + j + 1 + 1 > N:
            ans.append((i + 1, i + j + 1 + 1 - N))
        else:
            ans.append((i + 1, i + j + 1 + 1))
print("Yes")
for a, b in ans:
    print(a, b)
