S, T = input().split()
ans = "No"
for w in range(1, len(S)):
    A = [[] for _ in range(w)]
    for i in range(len(S)):
        A[i % w].append(S[i])
    for a in A:
        if "".join(a) == T:
            ans = "Yes"
            break
print(ans)
