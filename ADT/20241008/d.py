S, T = input().split()
ans = "No"
for k in range(1, len(S) - 1):
    M = [[] for _ in range(k)]
    for i, v in enumerate(S):
        M[i % k].append(v)
    for m in M:
        if "".join(m) == T:
            ans = "Yes"
print(ans)
