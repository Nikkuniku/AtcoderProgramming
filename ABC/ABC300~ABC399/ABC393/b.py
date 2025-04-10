S = input()
ans = 0
for j, v in enumerate(S):
    if v != "B":
        continue
    for d in range(1, len(S) + 1):
        i = j - d
        k = j + d
        if not (0 <= i < len(S) and 0 <= k < len(S)):
            break
        if S[i] == "A" and S[k] == "C":
            ans += 1
print(ans)
