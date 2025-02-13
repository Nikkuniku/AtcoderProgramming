S, T = input().split()
ans = "No"
for w in range(1, len(S)):
    R = [[] for _ in range(w)]
    for i, v in enumerate(S):
        R[i % w].append(v)
    for r in R:
        if "".join(r) == T:
            ans = "Yes"
print(ans)
